import operator

""" 
Defines a catalog for storing and retrieving operator functions based onn their symbols.
"""
class OperatorCatalog:
    def __init__(self):
        self.operators = {}
        
    def add(self, symbol, func):
        self.operators[symbol] = func
    
    def get(self, symbol):
        return self.operators.get(symbol)

    def check(self, symbol):
        return symbol in self.operators
    
DEFAULT_OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

catalog = OperatorCatalog()
for symbol, func in DEFAULT_OPERATORS.items():
    catalog.add(symbol, func)