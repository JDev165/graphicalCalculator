import unittest
import warnings
from stack import *


class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)

    def test_stack_push(self):
        expected_operators = ['÷', 'x', '+', '-', '(', ')']
        expression = '(2+2)x(2+2)'
        parsed_expression = ['']
        operators = LinkedListStack()
        operands = LinkedListStack()

        for token in expression:
            last_token = parsed_expression[-1]
            if (last_token.isdigit() or '.' in last_token or last_token == '') and (token not in expected_operators):
                parsed_expression[-1] += token
            else:
                parsed_expression.append(token)

        parsed_expression = ' '.join(parsed_expression)

        for token in parsed_expression:
            if token in expected_operators:
                operands.push(token)
            elif token != ' ':
                operators.push(token)

        operator = operators.tail
        index = 0
        while(operator.next):
            self.assertEqual(operator.value, parsed_expression[index])
            index += 1
            operator = operator.next
