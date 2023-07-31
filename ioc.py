from interfaces import ICommand


class IoC:
    @classmethod
    def resolve(cls, key, *args):
        return cls.strategy(key, *args)

    @staticmethod
    def _default_strategy(key, *args):
        if key == 'IoC.SetupStrategy':
            return SetupStrategyCommand(args[0])
        else:
            raise KeyError(f"Unknown dependency '{key}'")

    strategy = _default_strategy


class SetupStrategyCommand(ICommand):
    def __init__(self, new_strategy):
        self.new_strategy = new_strategy

    def execute(self) -> None:
        IoC.strategy = self.new_strategy
