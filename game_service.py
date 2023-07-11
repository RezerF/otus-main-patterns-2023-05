from abc import ABC, abstractmethod


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


class IMovable(ABC):
    @abstractmethod
    def get_position(self):
        ...

    @abstractmethod
    def get_velocity(self):
        ...

    @abstractmethod
    def set_position(self, a):
        return self


class IRotatable(ABC):
    @abstractmethod
    def get_direction(self):
        ...

    @abstractmethod
    def get_angular_velocity(self):
        ...

    @abstractmethod
    def get_direction_number(self):
        ...

    @abstractmethod
    def set_direction(self, a):
        return self


class SpaceShip(IMovable, IRotatable):
    def __init__(self, position=None, velocity=None, direction=None, direction_number=None, angular_velocity=None):
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.direction_number = direction_number
        self.angular_velocity = angular_velocity

    # @check
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


class MoveCommand:
    def __init__(self, movable: IMovable):
        self.movable = movable

    def execute(self):
        self.movable.set_position(
            VectorType.plus(
                self.movable.get_position(),
                self.movable.get_velocity()
            )
        )


class RotateCommand:
    def __init__(self, rotatable: IRotatable):
        self.rotatable = rotatable

    def execute(self):
        self.rotatable.set_direction(
            (
                    self.rotatable.get_direction() + self.rotatable.get_angular_velocity()
            ) % self.rotatable.get_direction_number()
        )


if __name__ == '__main__':
    print("Build success")