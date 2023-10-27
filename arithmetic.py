'''
ARTHIMETIC OPERATORS
This file contains Python classes that define the arithmetic operators for program synthesis.
'''

'''
CLASS DEFINITIONS
''' 

class IntegerVariable:
    '''
    Class to represent an integer variable. Note that position is the position of the variable in the input.
    For example, if the input is [4, 5, 6] and the variable is the third element (i.e., 6), then position = 2.
    '''
    def __init__(self, position):
        self.value = None           # value of the variable, initially None
        self.position = position    # position of the variable in the arguments to program
        self.type = int             # type of the variable

    def assign(self, value):
        self.value = value

class IntegerConstant:
    '''
    Class to represent an integer constant.
    '''
    def __init__(self, value):
        self.value = value  # value of the constant
        self.type = int     # type of the constant

class Add:
    '''
    Operator to add two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def __call__(self, x, y):
        return x + y
    
    def str(x, y):
        return f"{x} + {y}"

class Subtract:
    '''
    Operator to subtract two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def __call__(self, x, y):
        return x - y
    
    def str(x, y):
        return f"{x} - {y}"
    
class Multiply:
    '''
    Operator to multiply two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def __call__(self, x, y):
        return x * y
    
    def str(x, y):
        return f"{x} * {y}" 

class Divide:
    '''
    Operator to divide two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def __call__(self, x, y):
        try: # check for division by zero error
            return x / y
        except ZeroDivisionError:
            return None
    
    def str(x, y):
        return f"{x} / {y}"


'''
GLOBAL CONSTANTS
''' 

# define operators
arithmetic_operators = [Add(), Subtract(), Multiply(), Divide()]