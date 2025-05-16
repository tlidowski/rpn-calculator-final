from rpn_calculator.calculator import RPNCalculator
from rpn_calculator.operators import catalog

"""    
Defines a command line interface that allows users to enter operators and operands in Reverse Polish Notation and returns the value at the top of the stack.
"""

class CLICalculator:
    def __init__(self):
        self.calc = RPNCalculator(catalog)
    
    def start_cli(self):
        self.print_intro()
    
    def print_intro(self):
        print("- " * 30)
        print(
            "Welcome to the RPN CLI Calculator!\n\n",
            "INSTRUCTIONS:",
            "Enter values followed by an operator (e.g., `3 4 +`).\n",
            "You can input one at a time or multiple space-separated per line.\n",
            "Current operations suppoorted: " + " ".join(i for i in self.calc.catalog.operators) + "\n\n",
            "Press 'q' or Ctrl+D to exit.\n"
        )
        print("- " * 30)
