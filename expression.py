from stack import LinkedListStack

# Don't forget to add Python function annotations


class Expression:
    def __init__(self, exp):
        # DST = Data Structure
        self.expressionOperands = LinkedListStack()
        self.expressionOperators = LinkedListStack()
        self.expected_operators = {'÷': '/', 'x': '*',
                                   '+': '+', '-': '-', '(': '(', ')': ')'}
        self.exp = exp

    def evaluate(self):
        parsed_expression = self.parse()
        for token in parsed_expression:
            if token == ')':
                rightOperand = self.expressionOperands.pop()
                leftOperand = self.expressionOperands.pop()
                operator = self.expressionOperators.pop()

                result = self._performOperation(
                    leftOperand, rightOperand, operator)
                self._save(result, self.expressionOperands)
            elif token in self.expected_operators:
                token = self.expected_operators[token]
                self._save(token, self.expressionOperators)
            else:
                self._save(token, self.expressionOperands)

        finalResult = self.expressionOperands.pop()
        return finalResult

    def _performOperation(self, left, right, op):
        result = 0
        if op == '+':
            result = eval(left + right)
        elif op == '-':
            result = eval(left - right)
        elif op == '/':
            result = eval(left / right)
        else:
            result = eval(left * right)

        return result

    def _save(self, data, stack):
        stack.push(data)

    def parse(self):
        parsed_expression = ['']
        for token in self.exp:
            last_token = parsed_expression[-1]
            if (last_token.isdigit() or '.' in last_token or last_token == '') and (token not in self.expected_operators):
                parsed_expression[-1] += token
            else:
                parsed_expression.append(token)

        return parsed_expression


def main():
    exp = Expression('(2.05+20x(100÷2))x((5-2)+2)))')
    result = exp.evaluate()
    print(result)


if __name__ == "__main__":
    main()
