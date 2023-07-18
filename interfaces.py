from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self):
        ...


class IMovable(ABC):
    @abstractmethod
    def get_position(self):
        ...

    @abstractmethod
    def get_velocity(self):
        ...

    @abstractmethod
    def set_velocity(self, a):
        ...

    @abstractmethod
    def set_position(self, a):
        ...

    @abstractmethod
    def get_is_movable(self):
        ...

    @abstractmethod
    def set_is_movable(self, value: bool):
        ...


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
        ...


class IFuelable(ABC):
    @abstractmethod
    def get_fuel(self):
        ...

    @abstractmethod
    def get_burning_level(self):
        ...

    @abstractmethod
    def set_fuel(self, a):
        ...