'''
ARTHIMETIC OPERATORS
This file contains Python classes that define the arithmetic operators for program synthesis.
'''

'''
CLASS DEFINITIONS
''' 

class IntegerValue:
    '''
    Class to represent an arithmetic value.
    '''
    def __init__(self, value):
        self.value = value
        self.type = int

class Add:
    '''
    Operator to add two numerical values.
    '''
    def __init__(self):
        self.arity = 2          # number of arguments of function
        self.weight = 1         # weight of function
        self.return_type = int  # return type of function

    def __call__(self, x, y):
        return x + y
    
    def str(x, y):
        return f"{x} + {y}"

class Subtract:
    '''
    Operator to subtract two numerical values.
    '''
    def __init__(self):
        self.arity = 2          # number of arguments of function
        self.weight = 1         # weight of function
        self.return_type = int  # return type of function

    def __call__(self, x, y):
        return x - y
    
    def str(x, y):
        return f"{x} - {y}"
    
class Multiply:
    '''
    Operator to multiply two numerical values.
    '''
    def __init__(self):
        self.arity = 2          # number of arguments of function
        self.weight = 1         # weight of function
        self.return_type = int  # return type of function

    def __call__(self, x, y):
        return x * y
    
    def str(x, y):
        return f"{x} * {y}" 

class Divide:
    '''
    Operator to divide two numerical values.
    '''
    def __init__(self):
        self.arity = 2          # number of arguments of function
        self.weight = 1         # weight of function
        self.return_type = int  # return type of function

    def __call__(self, x, y):
        try: # check for division by zero error
            return x / y
        except ZeroDivisionError:
            return None
    
    def str(x, y):
        return f"{x} / {y}"


'''
FUNCTION DEFINITIONS
''' 


'''
GLOBAL CONSTANTS
''' 

# define operators
arithmetic_operators = [Add(), Subtract(), Multiply(), Divide()]