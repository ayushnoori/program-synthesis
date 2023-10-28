import streamlit as st

# standard imports
import numpy as np
import argparse
import itertools
import time

# import examples and synthesizer
from arithmetic import *
from strings import *
from abstract_syntax_tree import *
from examples import *
from synthesis import *
import config

# write streamlit title
st.title("Bottom-Up Program Synthesis")

st.markdown('''
Completed for [CS252R: Program Synthesis](https://synthesis.metareflection.club/) at the Harvard John A. Paulson School of Engineering and Applied Sciences, taught in Fall 2023 by Prof. Nada Amin.
''')

st.header("👨🏽‍💻 Project Description")

st.markdown('''
Here, we implement the non-ML subset of BUSTLE, the algorithm proposed by [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381). That is, we implement bottom-up enumerative search for simple compound expressions, excluding conditionals, recursion, and loops. The implementation is generic and flexibly supports multiple target languages. Arithmetic and string manipulations are natively supported, defined in `arithmetic.py` and `string.py`, respectively.
''')

st.subheader("Input-Output Examples")

st.markdown('''
Select input-output examples as defined in `examples.py`, or define your own custom examples. The examples are used to synthesize a satisfying program.
''')

# define variables
# domain = "arithmetic"
# examples_key = "addition"
# max_weight = 3
domain = st.selectbox("Domain", ["arithmetic", "strings"])
examples_key = st.selectbox("Examples", example_set.keys())
max_weight = st.slider("Maximum Weight", 2, 10, 3)

# retrieve selected input-output examples
examples = example_set[examples_key]

# extract constants from examples
st.subheader("Synthesis Steps")
program_bank = extract_constants(examples)
program_bank_str = [p.str() for p in program_bank]
print("\nSynthesis Log:")
print(f"- Extracted {len(program_bank)} constants from examples.")
st.markdown(f"* Extracted {len(program_bank)} constants from examples.")

# define operators
if domain == "arithmetic":
    operators = arithmetic_operators
elif domain == "strings":
    operators = string_operators
# else:
#     raise Exception('Domain not recognized. Must be either "arithmetic" or "string".')

# define final program
final_program = None

start_time = time.time()
# iterate over each level
for weight in range(2, max_weight):

    # print message
    print(f"- Searching level {weight} with {len(program_bank)} primitives.")
    st.markdown(f"* Searching level {weight} with {len(program_bank)} primitives.")

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
                final_program = program

end_time = time.time()
elapsed_time = round(end_time - start_time, 4)

# check if program was found
print("\nSynthesis Results:")
st.subheader("Synthesis Results")
if final_program is None:
    print(f"- Max weight of {max_weight} reached, no program found in {elapsed_time}s.")

    st.write(f":x: Max weight of {max_weight} reached, no program found in {elapsed_time}s.")
else:
    print(f"- Program found in {elapsed_time}s.")
    print(f"- Program: {final_program.str()}")
    print(f"- Program weight: {final_program.weight}")
    print(f"- Program return type: {final_program.type.__name__}")

    st.write(f":white_check_mark: Program found in {elapsed_time}s.")
    st.markdown(f"Program: `{final_program.str()}`")
    st.markdown(f"Weight: `{final_program.weight}`")
    st.markdown(f"Return Type: `{final_program.type.__name__}`")

st.header("🔎 Algorithm Details")

st.markdown('''
The most important data structure in this implementation is the abstract syntax tree (AST). The AST is a tree representation of a program, where each node is either a primitive or a compound expression. The AST is represented by the `OperatorNode` class in `abstract_syntax_tree.py`. My AST implementation includes functions to recursively evaluate the operator and its operands and also to generate a string representation of the program.

At program evaluation time, the AST is evaluated from the bottom up. That is, the operands are evaluated first, and then the operator is evaluated on the operands. This is implemented in the `evaluate` method of the `OperatorNode` class. In the case of integers, variable inputs are represented by the `IntegerVariable` class in `arithmetic.py`. When input is not `None`, input type checking and validation is performed by the `evaluate` function in this class.

The pseudocode for the bottom-up synthesis algorithm is reproduced below from [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381):
''')

st.image("https://github.com/ayushnoori/program-synthesis/assets/43010710/117e7797-11af-4b72-b5f4-dda95eb2260f")

st.markdown('''
Note that we do not consider the lines colored in blue (*i.e.*, lines 4, 16, and 17). For details on machine learning-guided bottom-up search, please see the [BUSTLE paper](https://arxiv.org/abs/2007.14381).
''')

st.header("📫 Contact")

st.markdown('''
Source code is publicly available via GitHub at [ayushnoori/program-synthesis](https://github.com/ayushnoori/program-synthesis). Any questions? Please feel free to reach out to Ayush Noori at [anoori@college.harvard.edu](mailto:anoori@college.harvard.edu).
''')

st.header("📖 References")

st.markdown('''
1. Odena, A. *et al.* [BUSTLE: Bottom-Up Program Synthesis Through Learning-Guided Exploration.](https://arxiv.org/abs/2007.14381) in *9th International Conference on Learning Representations*; 2021 May 3-7; Austria.
''')