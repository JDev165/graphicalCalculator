import unittest
import warnings
import stack
import expression


class TestLinkedListStack(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', category=DeprecationWarning)

    def test_stack_push(self):
        grouping_operators = ['(', ')']
        operators = stack.LinkedListStack()
        operands = stack.LinkedListStack()
        parsed_expression = expression.Expression('(2+2)x(2+2)').parse()
        expected_operators = ['+', 'x', '+']
        expected_operands = ['2', '2', '2', '2']

        results_operators = []
        results_operands = []

        for token in parsed_expression:
            if token in expected_operators:
                operators.push(token)
            elif token != '' and token not in grouping_operators:
                operands.push(token)

        node = operators.getTail()
        while(node):
            results_operators.append(node.value)
            node = node.next

        node = operands.getTail()
        while(node):
            results_operands.append(node.value)
            node = node.next

        self.assertTrue(results_operators == expected_operators)
        self.assertTrue(results_operands == expected_operands)

        del operands, operators

        # print(results_operators)
        # print(expected_operators)
        # print(results_operands)
        # print(expected_operands)


# def main():
#     test = TestLinkedListStack()
#     test.test_stack_push()


# if __name__ == "__main__":
#     main()
