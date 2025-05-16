from rpn_calculator.io_interfaces.cli import CLICalculator

def run_cli():
    new_calc = CLICalculator()
    new_calc.start_cli()

if __name__ == "__main__":
    run_cli()