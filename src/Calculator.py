#importing math module for squareroot function

import math

#defining calculator functions

def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    c = a - b
    return c

def multiplication(a, b):
    c = a * b
    return c

def division(a, b):
    c = a/b
    return c

def square(a, b):
    c = a ** b
    return c

def squareroot(a):
    sqrt_a = math.sqrt(a)
    return(sqrt_a)

#instantiating Calculator class

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result
    
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
    
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def squaring(self, a, b):
        self.result = square(a, b)
        return self.result
    
    def takesqrroot(self, a, b):
        self.result = squareroot(a, b)
        return self.result

