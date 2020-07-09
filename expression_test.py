import unittest
import warnings
from expression import Expression

class TestExpression(unittest.TestCase):

    def test_expression_evalutate(self):
        exp = Expression('(((2.05+20)x(100÷2))x((5-2)+2))')
        self.assertTrue(5512.5 == exp.evaluate())
        del exp
        exp = Expression('((2.55x6.1)÷2)')
        self.assertTrue(7.777499999999999 == exp.evaluate())
