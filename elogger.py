from interfaces import ICommand
import logging

logger = logging.getLogger(__name__)


class ELogger(ICommand):
    def __init__(self, cmd: ICommand, exc: Exception):
        self.cmd = cmd
        self.exc = exc

    def execute(self):
        logger.warning(f'Непредвиденная ошибка.\nCmd: {self.cmd.__class__.__name__}\nException: {self.exc}')
