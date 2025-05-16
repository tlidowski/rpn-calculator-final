from rpn_calculator.calculator import RPNCalculator
from rpn_calculator.operators import catalog

"""    
Defines a command line interface that allows users to enter operators and operands in Reverse Polish Notation and returns the value at the top of the stack.
"""

def run_cli():
    calc = RPNCalculator(catalog)
    print(
        "Welcome to the RPN CLI Calculator!\n\n"
        "INSTRUCTIONS:"
        "Enter values followed by an operator (e.g., `3 4 +`).\n"
        "You can input one at a time or multiple space-separated per line.\n"
        "Current operations suppoorted: " + " ".join(i for i in calc.catalog)
        "Press 'q' or Ctrl+D to exit.\n"
    )
