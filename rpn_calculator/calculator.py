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
            if self.catalog.check(item):
                if len(self.stack) < 2:
                    raise ValueError("Insufficient values in stack.")
                
                second = self.stack[-1]
                first = self.stack[-2]
                
                try: 
                    result = self.catalog.get(item)(first, second)
                except ZeroDivisionError:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                
                self.stack.pop()
                self.stack.pop()
                self.stack.append(result)
                
            else:
                try:
                    self.stack.append(float(item))
                except ValueError:
                    raise ValueError(f"Invalid input: {item}")

        if self.stack:
            return self.stack[-1]
        return None