import unittest
import warnings
import stack


class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)

    def test_stack_push(self):
        expected_operators = ['÷', 'x', '+', '-']
        expression = '(2+2)x(2+2)'
        parsed_expression = ['']
        operators = Stack()
        operands = Stack()

        for token in expression:
            last_token = parsed_expression[-1]
            if (last_token.isdigit() or '.' in last_token or last_token == '') and (token not in operators):
                parsed_expression[-1] += token
            else:
                parsed_expression.append(token)

        parsed_expression = ' '.join(parsed_expression)

        for token in parsed_expression:
        	if token in operators:
        		operands.push()
        	else:
        		operators.push()	       
