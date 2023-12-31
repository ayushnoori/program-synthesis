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
        self.position = position    # zero-indexed position of the variable in the arguments to program
        self.type = int             # type of the variable
        self.weight = 1             # weight of the variable

    def evaluate(self, input = None):

        # check that input is not None
        if input is None:
            raise ValueError("Input is None.")

        # check that input is a list
        if type(input) != list:
            raise ValueError("Input is not a list.")

        # check that input is not empty
        if len(input) == 0:
            raise ValueError("Input is empty.")

        # check that position is valid
        if self.position >= len(input):
            raise ValueError(f"Position {self.position} is out of range for input of length {len(input)}.")

        return input[self.position]
    
    def str(self):
        return f"x{self.position}"

class IntegerConstant:
    '''
    Class to represent an integer constant.
    '''
    def __init__(self, value):
        self.value = value  # value of the constant
        self.type = int     # type of the constant
        self.weight = 1     # weight of the constant

    def evaluate(self, input = None):
        return self.value
    
    def str(self):
        return str(self.value)

class Add:
    '''
    Operator to add two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x + y
    
    def str(self, x, y):
        return f"({x} + {y})"

class Subtract:
    '''
    Operator to subtract two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x - y
    
    def str(self, x, y):
        return f"({x} - {y})"
    
class Multiply:
    '''
    Operator to multiply two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x * y
    
    def str(self, x, y):
        return f"({x} * {y})" 

class Divide:
    '''
    Operator to divide two numerical values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [int, int]     # argument types
        self.return_type = int          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        try: # check for division by zero error
            return x / y
        except ZeroDivisionError:
            return None
    
    def str(self, x, y):
        return f"({x} / {y})"


'''
GLOBAL CONSTANTS
''' 

# define operators
arithmetic_operators = [Add(), Subtract(), Multiply(), Divide()]