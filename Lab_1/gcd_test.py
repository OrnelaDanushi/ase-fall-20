import calculator as c
import unittest


class TestGCD(unittest.TestCase):
    def test_gcd_integers_positive(self):
        result = c.gcd(6, 3)
        self.assertEqual(result, 3)

    def test_gcd_integers_positive2(self):
        result = c.gcd(7, 3)
        self.assertEqual(result, 1)

    def test_gcd_integers_negative(self):
        result = c.gcd(-6, -2)
        self.assertEqual(result, -2)

    def test_gcd_integers_negative2(self):
        result = c.gcd(-7, -2)
        self.assertEqual(result, -1)

    def test_gcd_integers_pos_neg(self):
        result = c.gcd(6, -2)
        self.assertEqual(result, -2)

    def test_gcd_integers_pos_neg2(self):
        result = c.gcd(9, -2)
        self.assertEqual(result, -1)

    def test_gcd_integers_neg_pos(self):
        result = c.gcd(-6, 2)
        self.assertEqual(result, 2)

    def test_gcd_integers_neg_pos2(self):
        result = c.gcd(-7, 2)
        self.assertEqual(result, 1)

    def test_gcd_zero(self):
        result = c.gcd(0, 2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
