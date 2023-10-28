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

# create class to hold arguments instead of arg-parser
class Args(object):
    pass
args = Args()

st.markdown('''
Completed for [CS252R: Program Synthesis](https://synthesis.metareflection.club/) at the Harvard John A. Paulson School of Engineering and Applied Sciences, taught in Fall 2023 by Prof. Nada Amin.
''')

st.header("👨🏽‍💻 Project Description")

st.markdown('''
Here, we implement the non-ML subset of BUSTLE, the algorithm proposed by [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381). That is, we implement bottom-up enumerative search for simple compound expressions, excluding conditionals, recursion, and loops. The implementation is generic and flexibly supports multiple target languages. Arithmetic and string manipulations are natively supported, defined in `arithmetic.py` and `string.py`, respectively.
''')

st.header("🔎 Algorithmic Description")

st.markdown('''
The most important data structure in this implementation is the abstract syntax tree (AST). The AST is a tree representation of a program, where each node is either a primitive or a compound expression. The AST is represented by the `OperatorNode` class in `abstract_syntax_tree.py`. My AST implementation includes functions to recursively evaluate the operator and its operands and also to generate a string representation of the program.

At program evaluation time, the AST is evaluated from the bottom up. That is, the operands are evaluated first, and then the operator is evaluated on the operands. This is implemented in the `evaluate` method of the `OperatorNode` class. In the case of integers, variable inputs are represented by the `IntegerVariable` class in `arithmetic.py`. When input is not `None`, input type checking and validation is performed by the `evaluate` function in this class.

The pseudocode for the bottom-up synthesis algorithm is reproduced below from [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381):

<img width="1494" alt="image" src="https://github.com/ayushnoori/program-synthesis/assets/43010710/117e7797-11af-4b72-b5f4-dda95eb2260f">

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