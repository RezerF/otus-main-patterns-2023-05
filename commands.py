import exceptions
from game_service import VectorType
from interfaces import ICommand, IMovable, IRotatable


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