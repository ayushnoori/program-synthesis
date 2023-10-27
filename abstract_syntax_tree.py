'''
ABSTRACT SYNTAX TREE
This file contains the Python class that defines the abstract syntax tree (AST) representation.
'''

class OperatorNode:
    '''
    Class to represent operator nodes (i.e., an operator and its operands) as an AST.

    Args:
        operator (object): operator object (e.g., Add, Subtract, etc.)
        children (list): list of children nodes (operands)
    
    Example:
        add_node = OperatorNode(Add(), [IntegerConstant(7), IntegerConstant(5)])
        subtract_node = OperatorNode(Subtract(), [IntegerConstant(3), IntegerConstant(1)])
        multiply_node = OperatorNode(Multiply(), [add_node, subtract_node])
        multiply_node.evaluate() # returns 24
        multiply_node.str() # returns "((7 + 5) * (3 - 1))"

        For variable computation, the input arguments are passed to the evaluate() method.
        For example, if instead:

        add_node = OperatorNode(Add(), [IntegerVariable(0), IntegerConstant(5)])
        multiply_node.evaluate([7]) # returns 24
    '''
    
    def __init__(self, operator, children):
        self.operator = operator  # Operator object (e.g., Add, Subtract, etc.)
        self.children = children  # list of children nodes (operands)

    def evaluate(self, input = None):

        # check arity of operator in AST
        if len(self.children) != self.operator.arity:
            raise ValueError("Invalid number of operands for operator")
        
        # recursively evaluate the operator and its operands
        operands = [child.evaluate(input) for child in self.children]
        return self.operator.evaluate(*operands, input)

    def str(self):

        # check arity of operator in AST
        if len(self.children) != self.operator.arity:
            raise ValueError("Invalid number of operands for operator")
        
        # recursively generate a string representation of the AST
        operand_strings = [child.str() for child in self.children]
        return self.operator.str(*operand_strings)