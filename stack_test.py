import unittest
import warnings
import stack


class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)

    def test_stack_push(self):
        expected_operators = ['÷', 'x', '+', '-']
        expression = '(2+2)*(2+2)'
        operators = Stack()
        operands = Stack()

        for value in expression:
            if value in expected_operators:
                operators.push(value)
            else if type(value) in [int, float]:
                operands.push(value)
            else:
                continue
