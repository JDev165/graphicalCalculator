# Don't forget to add Python function annotations


class Expression:
    def __init__(self, exp):
        # DST = Data Structure
        self.expressionDST = None
        self.expected_operators = ['÷', 'x', '+', '-', '(', ')']
        self.exp = exp

    def save(self, data):
        pass

    def parse(self):
        parsed_expression = ['']
        for token in self.exp:
            last_token = parsed_expression[-1]
            if (last_token.isdigit() or '.' in last_token or last_token == '') and (token not in self.expected_operators):
                parsed_expression[-1] += token
            else:
                parsed_expression.append(token)

        return parsed_expression

    def evaluate(self):
        pass

    def clear(self):
        pass
