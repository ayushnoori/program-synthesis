'''
EXAMPLES
This file contains input-output examples for both arithmetic and string domain-specific languages (DSLs).
To add a new example, add a new key to the dictionary 'example_set' and set the value to be a list of tuples.

Note that we synthesize programs with a consistent arity. Therefore, in each set of input-output examples, all 
input examples must be of the same length. Further, argument types must remain consistent across examples. We 
test for these conditions in the `check_examples` function below, which is called by the `extract_constants` 
function in the synthesizer.
'''

# define examples
example_set = {
    # basic arithmetic examples
    'addition': [([7, 2], 9), ([8, 1], 9), ([3, 9], 12), ([5, 8], 13)], # ([4, 6], 10), 
    'subtraction': [([9, 2], 7), ([6, 1], 5), ([7, 3], 4), ([8, 4], 4), ([10, 2], 8)],
    'multiplication': [([2, 3], 6), ([4, 5], 20), ([7, 8], 56), ([9, 2], 18), ([3, 4], 12)],
    'division': [([6, 2], 3), ([8, 4], 2), ([9, 3], 3), ([10, 5], 2), ([12, 6], 2)],

    # advanced arithmetic examples
    'add_5_multiply_2': [([1, 2], 12), ([3, 4], 22), ([5, 6], 32), ([7, 8], 42), ([9, 10], 52)],
    'multiply_add_9': [([1, 2], 11), ([3, 4], 21), ([5, 6], 39), ([7, 8], 65), ([9, 10], 9)],

    # basic string examples
    'concatenate': [(["a", "b"], "ab"), (["c", "d"], "cd"), (["e", "f"], "ef")],
    'right': [(["hello", 3], "llo"), (["world", 4], "orld"), (["fox", 1], "x")],
    'left': [(["hello", 2], "he"), (["world", 3], "wor"), (["fox", 2], "fo")],

    # advanced string examples
    'concatenate_3': [(["a", "b", "c"], "abc"), (["d", "e", "f"], "def"), (["g", "h", "i"], "ghi")],

    # custom user examples
}


# CHECK EXAMPLE VALIDITY
def check_examples(examples):
    '''
    Checks that all input examples are of same length and that argument types are consistent across examples.
    If valid, returns arity and argument types of function to be generated.

    Args:
        examples (list): list of tuples, where each tuple is of the form (input, output)
    
    Returns:
        input_lengths[0] (int): arity of function
        arg_types[0] (list): argument types of function
    '''

    # get input examples
    inputs = [example[0] for example in examples]

    # check all inputs are of same length
    input_lengths = [len(input) for input in inputs]
    if len(set(input_lengths)) != 1:
        raise ValueError("All input examples must be of same length.")

    # check that types of arguments are same
    arg_types = [[type(arg) for arg in input] for input in inputs]
    consistent_types = all([arg_types[0] == arg_type for arg_type in arg_types])
    if not consistent_types:
        raise ValueError("Argument types must be consistent across inputs.")
    
    # return arity and argument types
    return input_lengths[0], arg_types[0]