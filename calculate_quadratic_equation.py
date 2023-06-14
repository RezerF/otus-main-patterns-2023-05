ZERO = 0.00001


class QuadraticEquation:
    def __init__(self, a=1.0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
        self.discriminant = self.b ** 2 - 4 * self.a * self.c

    def check_arg(self):
        if -ZERO < self.a < ZERO:
            raise Exception("Arg \"a\" don't must be zero!")

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


if __name__ == '__main__':
    print("Build success")