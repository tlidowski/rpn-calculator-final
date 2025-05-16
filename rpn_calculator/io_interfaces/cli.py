from rpn_calculator.calculator import RPNCalculator
from rpn_calculator.operators import catalog

"""    
Defines a command line interface that allows users to enter operators and operands in Reverse Polish Notation and returns the value at the top of the stack.
"""

class CLICalculator:
    def __init__(self):
        self.calc = RPNCalculator(catalog)
    
    def start_cli(self):
        try:
            self.print_intro()
            while True: 
                num_input = input("> ")
                if num_input.strip().lower() in ('q'):
                    print("Closing RPN Calculator...")
                    break
                result = self.calc.evaluate(num_input)
                print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")
    
    def print_intro(self):
        supported_ops = " ".join(i for i in self.calc.catalog.operators)
        print("- " * 30)
        print(
            "Welcome to the RPN CLI Calculator!\n\n",
            "INSTRUCTIONS:",
            "Enter values followed by an operator (e.g., `3 4 +`).\n",
            "You can input one at a time or multiple space-separated per line.\n",
            f"Current operations supported: {supported_ops}\n\n",
            "Press 'q' or Ctrl+D to exit.\n"
        )
        print("- " * 30)
