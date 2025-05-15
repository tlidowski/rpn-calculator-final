from rpn_calculator.operators import catalog

"""    
Defines a Reverse Polish Notation calculator class that uses a stack-based approach wherre operands are pushed to a stack and pop the top values to be evaluated.
"""
class RPNCalculator:
    def __init__(self, op_catalog):
        self.catalog = op_catalog
        self.stack = []

    def evaluate(self, line):
        items = line.strip().split()

        for item in items:
            if self.catalog.contains(item):
                second = self.stack.pop()
                first = self.stack.pop()
                result = self.catalog.get(item)(first, second)
                self.stack.append(result)
            else:
                self.stack.append(float(item))

        if self.stack:
            return self.stack[-1]
        return None