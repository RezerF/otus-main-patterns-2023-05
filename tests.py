import unittest
from calculate_quadratic_equation import QuadraticEquation


class TestCalculateQuadraticEquation(unittest.TestCase):
    def test_not_sqr_root_empty_b(self):
        self.assertEqual(QuadraticEquation(a=1, c=1).solve(), [])

    def test_two_sqr_root_empty_b(self):
        self.assertEqual(QuadraticEquation(a=1, c=-1).solve(), [1.0, -1.0])

    def test_one_sqr_root(self):
        self.assertEqual(QuadraticEquation(1, 2, 1).solve(), [-1.0])

    def test_arg_a_not_zero(self):
        with self.assertRaises(Exception, msg="Arg \"a\" don't must be zero!"):
            QuadraticEquation(0, 2, 3).solve()

    def test_one_sqr_root_discriminant_less_than_epsilon(self):
        self.assertEqual(QuadraticEquation(1, 2.000001, 1).solve(), [-1.0000005])


if __name__ == '__main__':
    unittest.main()