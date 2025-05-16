import pytest
from rpn_calculator.calculator import RPNCalculator
from rpn_calculator.operators import catalog

"""
Unit tests using pytest to demonstrate intended behavior, prevent regressions, and withstand future changes.

Unit tests included: 
- Core functionality
- Error handling
- Input robustness
- Float precision
- Edge cases
"""

# --- Setup fixtures ---

@pytest.fixture
def calc():
    return RPNCalculator(catalog)

# --- Testing: Basic Arithmetic ---

def test_push_number(calc):
    assert calc.evaluate("3") == 3.0

def test_addition(calc):
    calc.evaluate("3")
    assert calc.evaluate("5 +") == 8.0

def test_subtraction(calc):
    calc.evaluate("10")
    assert calc.evaluate("2 -") == 8.0
    
def test_multiplication(calc):
    calc.evaluate("2")
    assert calc.evaluate("3 *") == 6.0

def test_int_division(calc):
    calc.evaluate("12")
    assert calc.evaluate("3 /") == 4.0

def test_float_division(calc):
    calc.evaluate("9")
    assert calc.evaluate("4 /") == 2.25
    
def test_negative_number(calc):
    assert calc.evaluate("-2") == -2.0
    assert calc.evaluate("5 +") == 3.0
    
def test_multiple_operations_separated(calc):
    calc.evaluate("5")
    calc.evaluate("8")
    assert calc.evaluate("+") == 13.0
    
def test_multiple_operations_inline(calc):
    assert calc.evaluate("5 5 5 8 + + -") == -13.0

def test_multiple_operations_inline_mixed(calc):
    assert calc.evaluate("5 1 2 + 4 * + 3 -") == 14.0
    

# --- Testing: Error Handling ---

def test_divide_by_zero(calc):
    calc.evaluate("10")
    calc.evaluate("0")
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        calc.evaluate("/")

def test_invalid_input(calc):
    with pytest.raises(ValueError, match=r"Invalid input: f"):
        calc.evaluate("3 f +")

def test_insufficient_values(calc):
    with pytest.raises(ValueError, match="Insufficient values in stack."):
        calc.evaluate("+")

def test_stack_after_value_error(calc):
    calc.evaluate("9")
    with pytest.raises(ValueError):
        calc.evaluate("+")
    assert calc.evaluate("1 +") == 10.0
    
def test_stack_after_zero_error(calc):
    calc.evaluate("10")
    calc.evaluate("0")
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        calc.evaluate("/")
    assert calc.evaluate("5 +") == 5.0