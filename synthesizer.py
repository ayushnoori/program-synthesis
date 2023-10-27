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

# import examples
from arithmetic import *
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


# RUN SYNTHESIZER
def run_synthesizer(args):
    '''
    Run bottom-up enumerative synthesis.
    '''

    # retrieve selected input-output examples
    examples = example_set[args.examples_key]

    # extract constants from examples
    program_bank = extract_constants(examples)
    print(examples)

    pass


if __name__ == '__main__':

    # parse command line arguments
    args = parse_args()
    # print(args)

    # run bottom-up enumerative synthesis
    run_synthesizer(args)
