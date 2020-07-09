import unittest
import warnings
import stack
import expression


class TestLinkedListStack(unittest.TestCase):

    def test_stack_pop(self):
        grouping_operators = ['(', ')']

        # test 1
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

        while(not operators.isEmpty()):
            results_operators.append(operators.pop())

        while(not operands.isEmpty()):
            results_operands.append(operands.pop())

        self.assertTrue(results_operators == expected_operators)
        self.assertTrue(results_operands == expected_operands)

        # print(results_operators)
        # print(expected_operators)
        # print(results_operands)
        # print(expected_operands)

        del operands, operators

        # Test 2
        operators = stack.LinkedListStack()
        operands = stack.LinkedListStack()
        parsed_expression = expression.Expression(
            '(2.05+20x(100÷2))x((5-2)+2))').parse()
        # In reverse order since Stacks are LIFO when popping
        expected_operators = ['+', '-', 'x', '÷', 'x', '+']
        expected_operands = ['2', '2', '5', '2', '100', '20', '2.05']
        results_operators = []
        results_operands = []

        for token in parsed_expression:
            if token in expected_operators:
                operators.push(token)
            elif token != '' and token not in grouping_operators:
                operands.push(token)

        while(not operators.isEmpty()):
            results_operators.append(operators.pop())

        while(not operands.isEmpty()):
            results_operands.append(operands.pop())

        self.assertTrue(results_operators == expected_operators)
        self.assertTrue(results_operands == expected_operands)

        # print(results_operators)
        # print(expected_operators)
        # print(results_operands)
        # print(expected_operands)

    def test_stack_push(self):
        grouping_operators = ['(', ')']

        # Test 1
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

        # Test 2

        operators = stack.LinkedListStack()
        operands = stack.LinkedListStack()
        parsed_expression = expression.Expression(
            '(2.05+20x(100÷2))x((5-2)+2))').parse()
        expected_operators = ['+', 'x', '÷', 'x', '-', '+']
        expected_operands = ['2.05', '20', '100', '2', '5', '2', '2']
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


def main():
    test = TestLinkedListStack()
    test.test_stack_pop()


if __name__ == "__main__":
    main()
