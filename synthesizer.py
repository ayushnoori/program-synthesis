'''
BOTTOM UP ENUMERATIVE SYNTHESIS
Ayush Noori
CS252R, Fall 2020

Example of usage:
python synthesizer.py --domain arithmetic --examples addition
'''

# load libraries
import numpy as np
import argparse
import itertools
import time

# import examples
from arithmetic import *
from abstract_syntax_tree import *
from examples import example_set, check_examples
import config


# PARSE ARGUMENTS
def parse_args():
    '''
    Parse command line arguments.
    '''

    parser = argparse.ArgumentParser(description="Bottom-up enumerative synthesis in Python.")

    # define valid choices for the 'domain' argument
    valid_domain_choices = ["arithmetic", "string"]

    # add examples
    parser.add_argument('--domain', type=str, required=True, # default="arithmetic",
                        choices=valid_domain_choices,
                        help='Domain of synthesis (either "arithmetic" or "string").')

    parser.add_argument('--examples', dest='examples_key', type=str, required=True, # default="addition",
                        choices=example_set.keys(),
                        help='Examples to synthesize program from. Must be a valid key in the "example_set" dictionary.')
    
    parser.add_argument('--max_weight', type=int, required=False, default=3,
                        help='Maximum weight of programs to consider before terminating search.')

    args = parser.parse_args()
    return args


# EXTRACT CONSTANTS AND VARIABLES
def extract_constants(examples):
    '''
    Extracts the constants from the input-output examples. Also constructs variables as needed
    based on the input-output examples, and adds them to the list of constants.
    '''

    # check validity of provided examples
    # if valid, extract arity and argument types
    arity, arg_types = check_examples(examples)

    # initialize list of constants
    constants = []

    # get unique set of inputs
    inputs = [input for example in examples for input in example[0]]
    inputs = set(inputs)

    # add 1 to the set of inputs
    inputs.add(1)

    # extract constants in input
    for input in inputs:

        if type(input) == int:
            constants.append(IntegerConstant(input))
        elif type(input) == str:
            # constants.append(StringConstant(input))
            pass
        else:
            raise Exception("Input of unknown type.")
        
    # initialize list of variables
    variables = []

    # extract variables in input
    for position, arg in enumerate(arg_types):
        if arg == int:
            variables.append(IntegerVariable(position))
        elif arg == str:
            # variables.append(StringVariable(position))
            pass
        else:
            raise Exception("Input of unknown type.")

    return constants + variables


# CHECK OBSERVATIONAL EQUIVALENCE
def observationally_equivalent(program_a, program_b, examples):
    """
    Returns True if Program A and Program B are observationally equivalent, False otherwise.
    """

    inputs = [example[0] for example in examples]
    a_output = [program_a.evaluate(input) for input in inputs]
    b_output = [program_b.evaluate(input) for input in inputs]

    return a_output == b_output


# CHECK CORRECTNESS
def check_program(program, examples):
    '''
    Check whether the program satisfies the input-output examples.
    '''
    
    inputs = [example[0] for example in examples]
    outputs = [example[1] for example in examples]
    program_output = [program.evaluate(input) for input in inputs]

    return program_output == outputs


# RUN SYNTHESIZER
def run_synthesizer(args):
    '''
    Run bottom-up enumerative synthesis.
    '''

    # retrieve selected input-output examples
    examples = example_set[args.examples_key]

    # extract constants from examples
    program_bank = extract_constants(examples)
    program_bank_str = [p.str() for p in program_bank]
    print(f"- Extracted {len(program_bank)} constants from examples.")

    # define operators
    operators = arithmetic_operators

    # iterate over each level
    for weight in range(2, args.max_weight):

        # print message
        print(f"- Searching level {weight} with {len(program_bank)} primitives.")

        # iterate over each operator
        for op in operators:

            # get all possible combinations of primitives in program bank
            combinations = itertools.combinations(program_bank, op.arity)

            # iterate over each combination
            for combination in combinations:

                # get type signature
                type_signature = [p.type for p in combination]

                # check if type signature matches operator
                if type_signature != op.arg_types:
                    continue

                # check that sum of weights of arguments <= w
                if sum([p.weight for p in combination]) > weight:
                    continue

                # create new program
                program = OperatorNode(op, combination)

                # check if program is in program bank using string representation
                if program.str() in program_bank_str:
                    continue
                
                # check if program is observationally equivalent to any program in program bank
                if any([observationally_equivalent(program, p, examples) for p in program_bank]):
                    continue

                # add program to program bank
                program_bank.append(program)
                program_bank_str.append(program.str())

                # check if program passes all examples
                if check_program(program, examples):
                    return(program)    

    # return None if no program is found
    return None 


if __name__ == '__main__':

    # parse command line arguments
    args = parse_args()
    # print(args)

    # run bottom-up enumerative synthesis
    start_time = time.time()
    program = run_synthesizer(args)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 4)

    # check if program was found
    if program is None:
        print(f"Max weight of {args.max_weight} reached, no program found in {elapsed_time}s.")
    else:
        print(f"Program found in {elapsed_time}s.")
        print(f"Program: {program.str()}")
        print(f"Program weight: {program.weight}")
        print(f"Program return type: {program.type.__name__}")
