class ENonePositionVelocityError(Exception):
    """Исклюение при получении не определенного значение координат"""


class EObjectNotMoveableError(Exception):
    """Исклюение при попытке сдвинуть не перемещаемый объект"""


class CommonException(Exception):
    """Общее исключение"""