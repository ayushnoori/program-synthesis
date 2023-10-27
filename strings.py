'''
STRING OPERATORS
This file contains Python classes that define the string operators for program synthesis.
'''

'''
CLASS DEFINITIONS
''' 

class StringVariable:
    '''
    Class to represent an string variable. Note that position is the position of the variable in the input.
    For example, if the input is ["a", "b", "c"] and the variable is the third element (i.e., "c"), then position = 2.
    '''
    def __init__(self, position):
        self.position = position    # zero-indexed position of the variable in the arguments to program
        self.type = str             # type of the variable
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

class StringConstant:
    '''
    Class to represent an string constant.
    '''
    def __init__(self, value):
        self.value = value  # value of the constant
        self.type = str     # type of the constant
        self.weight = 1     # weight of the constant

    def evaluate(self, input = None):
        return self.value
    
    def str(self):
        return str(self.value)

class Concatenate:
    '''
    Operator to concatenate two string values.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [str, str]     # argument types
        self.return_type = str          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x + y
    
    def str(self, x, y):
        return f"Concat({x}, {y})"

class Left:
    '''
    Operator to get left substring.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [str, int]     # argument types
        self.return_type = str          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x[:y]
    
    def str(self, x, y):
        return f"Left({x}, {y})"
    
class Right:
    '''
    Operator to get right substring.
    '''
    def __init__(self):
        self.arity = 2                  # number of arguments
        self.arg_types = [str, int]     # argument types
        self.return_type = str          # return type
        self.weight = 1                 # weight

    def evaluate(self, x, y, input = None):
        return x[(y * -1):]
    
    def str(self, x, y):
        return f"Right({x}, {y})" 


'''
GLOBAL CONSTANTS
''' 

# define operators
string_operators = [Concatenate(), Left(), Right()]