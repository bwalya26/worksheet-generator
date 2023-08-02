import random, string, math
import IPython
from IPython.display import display
import sympy
from sympy import *
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy import evaluate
import contextlib
from contextlib import redirect_stdout

class Quadratic():
    """A class to generate random algebraic expressions"""
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        
    def coeffient_one(self):
        """we set the value of the first coefficient equal to a as will we set a to random number"""
        coefficient_1 = self.a
        return coefficient_1
    
    def coeffient_two(self, a):
        """we set the value of the second coefficient equal to b as will we set b to random number"""
        coefficient_2 = self.a*b
        return coefficient_2
    
    def coeffient_three(self):
        """we set the value of the third coefficient equal to c as will we set c to random number"""
        coefficient_3 = self.c
        return coefficient_3
    
    def coeffient_four(self):
        """we set the value of the first coefficient equal to e as will we set e to random number"""
        coefficient_4 = self.e
        return coefficient_4
    
    def coeffient_five(self):
        """we set the value of the first coefficient equal to a as will we set a to random number"""
        coefficient_5 = self.f
        return coefficient_5
    
    def signs(self):
        """we set the value of the fourth coefficient equal to d as will we set d to random number"""
        signs_1 = self.d
        return signs_1
    
