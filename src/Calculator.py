# importing math module for squareroot function

import math


# defining calculator functions

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def square(a):
    return a**2


def squareroot(a):
    sqrt_a = math.sqrt(a)
    return sqrt_a


# instantiating Calculator class

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)

    def subtract(self, a, b):
        self.result = a - b
        return subtraction(a, b)

    def multiply(self, a, b):
        self.result = a * b
        return multiplication(a, b)

    def divide(self, a, b):
        self.result = a / b
        return division(a, b)

    def squaring(self, a):
        self.result = a**2
        return square(a)

    def takesqrroot(self, a):
        self.result = squareroot(a)
        return self.result
