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

def test_push_number_multiple(calc):
    result = calc.evaluate("2 3")
    assert result == 3.0

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
    
def test_multiple_operations_chained(calc):
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
    
# --- Testing: Unique Input Handling ---

def test_empty_input(calc):
    assert calc.evaluate("   ") is None
    assert calc.evaluate("") is None

def test_whitespace_tolerance(calc):
    assert calc.evaluate("   2    3   +  ") == 5.0

def test_unicode_input(calc):
    with pytest.raises(ValueError):
        calc.evaluate("π")

# --- Testing: Float Precision ---

def test_float_precision_addition(calc):
    result = calc.evaluate("0.1 0.2 +")
    assert abs(result - 0.3) < 1e-10

def test_float_precision_division(calc):
    result = calc.evaluate("1 3 /")
    assert abs(result - (1/3)) < 1e-10
    
def test_float_precision_multiplication(calc):
    result = calc.evaluate("1.1 2 *")
    assert abs(result - 2.2) < 1e-10


# --- Testing: Edge Cases ---

def test_large_input(calc):
    line = "1 " * 1000
    line += "+ " * 999
    assert calc.evaluate(line) == 1000.0

def test_extreme_value(calc):
    calc.evaluate("1e300")
    calc.evaluate("1")
    result = calc.evaluate("+")
    assert result >= 1e300

def test_negative_zero(calc):
    assert calc.evaluate("-0") == 0.0