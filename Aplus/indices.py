import random, string, math
import IPython
from IPython.display import display
import sympy
from sympy import *
from sympy.abc import a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
from sympy import evaluate
import contextlib
from contextlib import redirect_stdout

class Evaluate():
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
    
    def coeffient_two(self):
        """we set the value of the second coefficient equal to b as will we set b to random number"""
        coefficient_2 = self.b
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
    
class Simplify():
    """A class to generate random algebraic expressions"""
    def __init__(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.n = n
        
    def coeffient_one(self):
        """we set the value of the first coefficient equal to a as will we set a to random number"""
        coefficient_1 = self.a
        return coefficient_1
    
    def coeffient_two(self):
        """we set the value of the second coefficient equal to b as will we set b to random number"""
        coefficient_2 = self.b
        return coefficient_2
    
    def coeffient_three(self):
        """we set the value of the third coefficient equal to c as will we set c to random number"""
        coefficient_3 = self.c
        return coefficient_3
    
    def coeffient_four(self):
        """we set the value of the fourth coefficient equal to d as will we set d to random number"""
        coefficient_4 = self.d**2
        return coefficient_4
    
    def constant_term(self):
        """we set the value of the firth coefficient equal to e as will we set e to random number"""
        constant_1 = (self.e*self.d)**2
        return constant_1

    def coeffient_five(self):
        """we set the value of the first coefficient equal to a as will we set a to random number"""
        coefficient_5 = self.k
        return coefficient_5
    
    def coeffient_six(self):
        """we set the value of the second coefficient equal to b as will we set b to random number"""
        coefficient_6 = self.l * self.k
        return coefficient_6
    
    def coeffient_seven(self):
        """we set the value of the third coefficient equal to c as will we set c to random number"""
        coefficient_7 = self.m
        return coefficient_7
    
    def coeffient_eight(self):
        """we set the value of the fourth coefficient equal to d as will we set d to random number"""
        coefficient_8 = self.n
        return coefficient_8
        
    def coeffient_nine(self):
        """we set the value of the fourth coefficient equal to d as will we set d to random number"""
        coefficient_8 = self.o
        return coefficient_9
    
    
    def term_one(self):
        """we set the value of the first term equal to f as will we set f to random term"""
        term_1 = self.f
        return term_1
    
    def term_two(self):
        """we set the value of the second term equal to g as will we set g to random term"""
        term_2 = self.g
        return term_2
    
    def term_three(self):
        """we set the value of the third term equal to h as will we set h to random number"""
        coefficient_3 = self.c
        return coefficient_3
    
    def term_four(self):
        """we set the value of the fourth term equal to i as will we set i to random term"""
        term_4 = self.i
        return term_4
    
    def term_five(self):
        """we set the value of the firth cterm equal to j as will we set j to random term"""
        term_5 = self.j
        return term_5
    
class QuadraticEquationSolver():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def coefficient_1(self):
        coefficient_1 = self.a
        return coefficient_1
    
    def coefficient_2(self):
        coefficient_2 = self.b
        return coefficient_2
        
    def coefficient_3(self):
        coefficient_3 = self.c
        return coefficient_3
        
