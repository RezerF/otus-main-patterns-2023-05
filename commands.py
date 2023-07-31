from typing import Union

import exceptions
from game_service import VectorType
from interfaces import ICommand, IMovable, IRotatable, IFuelable


class MacroCommand(ICommand):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        try:
            for cmd in self.commands:
                cmd.execute()
        except Exception as e:
            raise exceptions.CommonException(e)


class MoveCommand(ICommand):
    def __init__(self, movable: IMovable):
        self.movable = movable

    def execute(self):
        if not self.movable.get_is_movable():
            raise exceptions.EObjectNotMoveableError
        if None in self.movable.get_position():
            raise exceptions.ENonePositionVelocityError
        if None in self.movable.get_velocity():
            raise exceptions.ENonePositionVelocityError
        self.movable.set_position(
            VectorType.plus(
                self.movable.get_position(),
                self.movable.get_velocity()
            )
        )


class RotateCommand(ICommand):
    def __init__(self, rotatable: IRotatable):
        self.rotatable = rotatable

    def execute(self):
        self.rotatable.set_direction(
            (
                    self.rotatable.get_direction() + self.rotatable.get_angular_velocity()
            ) % self.rotatable.get_direction_number()
        )


class CheckFuelCommand(ICommand):
    def __init__(self, f: IFuelable):
        self.f = f

    def execute(self):
        if self.f.get_fuel() < self.f.get_burning_level():
            raise exceptions.CommonException('Not enough fuel')
        return True


class BurnFuelCommand(ICommand):
    def __init__(self, f: IFuelable):
        self.f = f

    def execute(self):
        self.f.set_fuel(self.f.get_fuel() - self.f.get_burning_level())


class ChangeVelocityCommand(ICommand):
    def __init__(self, obj: Union[IRotatable, IMovable]):
        self.obj = obj

    def execute(self):
        try:
            self.obj.set_velocity(self.obj.get_velocity().half())
        except Exception as e:
            raise exceptions.CommonException(e)


class RotateWithChangeVelocity(ICommand):
    def __init__(self, obj: Union[IRotatable, IMovable]):
        self.obj = obj

    def execute(self) -> None:
        MacroCommand([
            RotateCommand(self.obj),
            ChangeVelocityCommand(self.obj)
        ]).execute()


class Retry(ICommand):
    def __init__(self, cmd: ICommand):
        self.cmd = cmd

    def execute(self) -> None:
        self.cmd.execute()


class DoubleRetry(ICommand):
    def __init__(self, cmd: ICommand):
        self.cmd = cmd

    def execute(self) -> None:
        self.cmd.execute()
