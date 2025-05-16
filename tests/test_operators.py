import pytest
import operator
from rpn_calculator.operators import OperatorCatalog

"""
Unit tests using pytest to demonstrate intended behavior, prevent regressions, and withstand future changes.

Unit tests included: 
- Catalog creation
- Addition & retrieval
"""

# --- Setup fixtures ---

@pytest.fixture
def log():
    return OperatorCatalog()

# --- Testing: Catalog Creation ---

def test_catalog_initialization(log):
    assert isinstance(log.operators, dict)
    assert len(log.operators) == 0

# --- Testing: Operator Addition & Retrieval ---

def test_get_default_operator(log):
    log.add('+', operator.add)
    assert log.get('+') is operator.add

def test_add_new_operator(log):
    log.add('^', pow)
    assert log.get('^') is pow

def test_get_nonexistent_operator(log):
    assert log.get('%') is None

def test_operator_check(log):
    log.add('%', operator.mod)
    assert log.check('%') is True
    assert log.check('^') is False
