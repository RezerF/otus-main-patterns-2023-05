import pytest

from game_service import SpaceShip, MoveCommand, VectorType, RotateCommand


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

