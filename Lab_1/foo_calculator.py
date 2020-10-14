# make a class which exploits the module calculator
import calculator as c


class foo_calculator:
    def __init__(self):
        # empty constructor,
        # in which self is a formal argument, it passes itself
        pass

    def sum(self, m, n):
        return c.sum(m, n)

    def divide(self, m, n):
        return c.divide(m, n)

    def subtract(self, m, n):
        return c.subtract(m, n)

    def multiply(self, m, n):
        return c.multiply(m, n)

    def gcd(self, m, n):
        return c.gcd(m, n)


fc = foo_calculator()
print(fc.sum(10, 10))
print(fc.sum(10, -10))
print(fc.divide(-10, 5))
print(fc.divide(10, -5))
print(fc.divide(10, 5))
print(fc.subtract(10, 5))
print(fc.multiply(10, 5))
print(fc.gcd(10, 5))
