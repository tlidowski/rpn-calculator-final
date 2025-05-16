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
            self.run_calc()
        except EOFError:
            self.handle_exit("Received EOF (Ctrl+D). Closing RPN Calculator...")
        except KeyboardInterrupt:
            self.handle_exit("Received keyboard interrupt (Ctrl+C). Closing RPN Calculator...")
        except Exception as e:
            self.handle_exit(f"Unexpected error: {e}")
    
    def run_calc(self):
        while True:
            try:
                num_input = input("> ")
                if num_input.strip().lower() == "q":
                    self.handle_exit("Closing RPN Calculator...")
                    exit()
                result = self.calc.evaluate(num_input)
                print(f"= {result}")
            except ValueError as ve:
                self.handle_exit(f"Input error: {ve}")
            except ZeroDivisionError:
                self.handle_exit("Math error: Division by zero is not allowed.")
    
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

    def handle_exit(self, message):
        print(f"\n{message}")