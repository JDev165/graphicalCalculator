import unittest
import warnings
from expression import Expression

class TestExpression(unittest.TestCase):

    def test_expression_evalutate(self):
        # Need to handle cases like ((1*1)*(1))
        # Stack is empty after we evaulate (1) so we see
        # the last ')', and that triggers a pop on empty stack
        exp = Expression('(((2.05+20)x(100÷2))x((5-2)+2))')
        self.assertTrue(5512.5 == exp.evaluate())
        del exp
        exp = Expression('((2.55x6.1)÷2)')
        self.assertTrue(7.777499999999999 == exp.evaluate())
        del exp
        exp = Expression('(((2.21x4.1)÷2)x0)')
        self.assertTrue(0 == exp.evaluate())
        del exp
        exp = Expression('(((1x1)x1)x1)')
        self.assertTrue(1 == exp.evaluate())
        del exp
        exp = Expression('(5+10)')
        self.assertTrue(15 == exp.evaluate())
        del exp
        exp = Expression('(((5+10)x10)÷10)')
        self.assertTrue(15 == exp.evaluate())
        del exp
        exp = Expression('((((5+10)x10)÷10)-(200.2x2))')
        self.assertTrue(-385.4 == exp.evaluate())
        del exp
