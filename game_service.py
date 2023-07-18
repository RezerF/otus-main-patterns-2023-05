from interfaces import IMovable, IRotatable


class VectorType:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __eq__(self, other):
        # for tests compare objects
        if not isinstance(other, VectorType):
            return NotImplemented

        return self.x == other.x and self.y == other.y

    @staticmethod
    def plus(position, velocity):
        x, y = position
        dx, dy = velocity
        return VectorType(x + dx, y + dy)

    def half(self):
        return VectorType(self.x / 2, self.y / 2)


class SpaceShip(IMovable, IRotatable):
    def __init__(self, position=None, velocity=None, direction=None, direction_number=None, angular_velocity=None,
                 is_movable=True):
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.direction_number = direction_number
        self.angular_velocity = angular_velocity
        self.is_movable = is_movable

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def set_position(self, new_value):
        self.position = new_value

    def get_direction(self):
        return self.direction

    def get_direction_number(self):
        return self.direction_number

    def get_angular_velocity(self):
        return self.angular_velocity

    def set_direction(self, value):
        self.direction = value

    def get_is_movable(self):
        return self.is_movable

    def set_is_movable(self, value: bool):
        self.is_movable = value

    def set_velocity(self, new_value):
        self.velocity = new_value


if __name__ == '__main__':
    print("Build success")
