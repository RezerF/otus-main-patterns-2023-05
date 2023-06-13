ZERO = 0.00001


class QuadraticEquation:
    def __init__(self, a=1.0, b=1, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    # def discriminant(self):
    #     return self.b ** 2 - 4 * self.a * self.c

    def check_arg(self):
        if -ZERO < self.a < ZERO:
            raise Exception("'a' не может быть равна 0")

    def is_root(self):
        if self.discriminant < 0:
            return False
        return True

    def get_one_root(self):
        return [- 1 * self.b / (2 * self.a)]

    def get_two_root(self):
        x1 = (- 1 * self.b + self.discriminant ** 0.5) / (2 * self.a)
        x2 = (- 1 * self.b - self.discriminant ** 0.5) / (2 * self.a)
        return [x1, x2]

    def solve(self):
        self.check_arg()
        if self.is_root():
            if -ZERO < self.discriminant < ZERO:
                return self.get_one_root()
            else:
                return self.get_two_root()
        return []


def test1():
    # 2*x**2 + 2*x + 3 = 0
    x = QuadraticEquation(2, 2, 3)
    return x.solve()


def test2():
    x = QuadraticEquation(-4, 28, -49)
    return x.solve()


def test3():
    x = QuadraticEquation(1, 2, 1)
    return x.solve()


def test4():
    x = QuadraticEquation(1, 0, 1)
    return x.solve()


def test5():
    x = QuadraticEquation(1, 0, -1)
    return x.solve()


def test6():
    x = QuadraticEquation(0.000, 0, -1)
    return x.solve()


print(test1(), test2(), test3(), test4(), test5(), test6(), sep="\n")
pass
