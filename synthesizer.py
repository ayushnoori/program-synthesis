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
from examples import examples
import config


def parse_args(examples):
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
                        choices=examples.keys(),
                        help='Examples to synthesize program from. Must be a valid key in the "examples" dictionary.')
    
    parser.add_argument('--max_weight', type=int, required=False, default=3,
                        help='Maximum weight of programs to consider before terminating search.')

    args = parser.parse_args()
    return args


if __name__ == '__main__':

    # parse command line arguments
    args = parse_args(examples)
    print(args.domain)
    print(args.examples_key)
    print(args.max_weight)

    # run bottom-up enumerative synthesis
    # run_synthesizer(args)
