from unittest.mock import Mock

import pytest

import exceptions
from commands import MoveCommand, RotateCommand, CheckFuelCommand, BurnFuelCommand, MacroCommand, ChangeVelocityCommand
from game_service import SpaceShip, VectorType
from interfaces import IFuelable, ICommand, IRotatable, IMovable


class TestMoveObject:
    @pytest.mark.parametrize("position, velocity, expected_position", [
        ((12, 5), (-7, 3), (5, 8)),
        ((0, 0), (+7, -3), (7, -3)),
    ])
    def test_move_ship(self, position, velocity, expected_position):
        ship = SpaceShip(position, velocity)
        move = MoveCommand(ship)
        move.execute()
        expected_position = VectorType(*expected_position)

        assert ship.position == expected_position

    @pytest.mark.parametrize(
        ('position', 'velocity', 'is_movable', 'expected_exception'),
        [
            ((None, 5), (-7, 3), True, exceptions.ENonePositionVelocityError),
            ((12, 5), (None, 3), True, exceptions.ENonePositionVelocityError),
            ((12, 5), (-7, 3), False, exceptions.EObjectNotMoveableError),
        ],
    )
    def test_move_exceptions(self, position, velocity, is_movable, expected_exception):
        ship = SpaceShip(position, velocity, is_movable=is_movable)
        with pytest.raises(expected_exception):
            MoveCommand(ship).execute()


class TestRotateObject:
    @pytest.mark.parametrize("direction, direction_number, angular_velocity, result_direction", [
        (2, 7, 1, 3),
        (3, 5, 3, 1),
        (3, 36, -3, 0),
        (2, 8, -4, 6),
    ])
    def test_rotate_ship(self, direction, direction_number, angular_velocity, result_direction):
        ship = SpaceShip(direction=direction, direction_number=direction_number, angular_velocity=angular_velocity)
        rotate = RotateCommand(ship)
        rotate.execute()
        assert ship.direction == result_direction


class TestCheckFuelCommand:
    @pytest.mark.parametrize("fuel, burning_level", [
        (2, 1),
        (3, 3),
        (5, 4),
        (0, 0),
    ])
    def test_check_fuel_enough(self, fuel, burning_level):
        fuelable_obj = Mock(IFuelable)
        fuelable_obj.get_fuel.return_value = fuel
        fuelable_obj.get_burning_level.return_value = burning_level
        assert CheckFuelCommand(fuelable_obj).execute()

    @pytest.mark.parametrize("fuel, burning_level", [
        (1, 2),
        (0, 3),
        (5, 5.1),
    ])
    def test_check_fuel_not_enough(self, fuel, burning_level):
        fuelable_obj = Mock(IFuelable)
        fuelable_obj.get_fuel.return_value = fuel
        fuelable_obj.get_burning_level.return_value = burning_level
        with pytest.raises(exceptions.CommonException):
            CheckFuelCommand(fuelable_obj).execute()


class TestBurnFuelCommand:
    @pytest.mark.parametrize("fuel, burning_level, expected_result", [
        (2, 1, 1),
        (3, 3, 0),
        (5, 4, 1),
        (0, 0, 0),
    ])
    def test_burn_fuel(self, fuel, burning_level, expected_result):
        fuelable_obj = Mock(IFuelable)
        fuelable_obj.get_fuel.return_value = fuel
        fuelable_obj.get_burning_level.return_value = burning_level
        BurnFuelCommand(fuelable_obj).execute()
        fuelable_obj.set_fuel.assert_called_with(expected_result)


class TestMacroCommand:
    @pytest.mark.parametrize("count", [1, 3, 7])
    def test_macro_command_execute(self, count):
        cmds = [Mock(ICommand) for i in range(count)]
        MacroCommand(cmds).execute()

    def test_macro_command_execute_error(self):
        cmds = [Mock(ICommand) for i in range(3)]
        cmds[1].execute.side_effect = UnicodeError('Unicode error unexpect')

        with pytest.raises(exceptions.CommonException):
            MacroCommand(cmds).execute()


class TestChangeVelocityCommand:
    @pytest.mark.parametrize("velocity, expected_velocity", [((1, 3), (0.5, 1.5)), ((2, 2), (1, 1)), ((0, 0), (0, 0))])
    def test_velocity_movable(self, velocity, expected_velocity):
        mock = Mock(IMovable, IRotatable)
        mock.get_velocity.return_value = VectorType(*velocity)
        ChangeVelocityCommand(mock).execute()
        mock.set_velocity.assert_called_with(VectorType(*expected_velocity))

    @pytest.mark.parametrize("velocity", [(None, 3), (2, None), (None, None)])
    def test_exception_velocity_movable(self, velocity):
        mock = Mock(IMovable, IRotatable)
        mock.get_velocity.return_value = VectorType(*velocity)
        with pytest.raises(exceptions.CommonException):
            ChangeVelocityCommand(mock).execute()
