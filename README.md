---
title: Program Synthesis
emoji: 🤗
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.19.0
app_file: app.py
pinned: false
---

# Bottom-Up Enumerative Program Synthesis

Completed for [CS252R: Program Synthesis](https://synthesis.metareflection.club/) at the Harvard John A. Paulson School of Engineering and Applied Sciences, taught in Fall 2023 by Prof. Nada Amin.

## 📢 Live Demonstration

Live demonstration available at:

<div align="center">
<a href = 'https://huggingface.co/spaces/ayushnoori/program-synthesis'><strong>https://huggingface.co/spaces/ayushnoori/program-synthesis</strong></a>
</div>

## 🛠️ Background

The following notes are adapted from [*Introduction to Program Synthesis*](http://people.csail.mit.edu/asolar/SynthesisCourse/TOC.htm) by Armando Solar-Lezama.

> In inductive synthesis, the goal is to generate a function that matches a given set of input/output examples. The simplest bottom up synthesis algorithm works by explicitly constructing all possible programs from a grammar starting with the terminals in the language. As one can imagine, this can be very inefficient, since the space of all expressions grows very large even with very small programs. The key idea behind this algorithm is to prune the set of primitives at every step by eliminating those that are deemed to be "observationally equivalent"; *i.e*., those which produce the same outputs on those inputs that were given as a specification. The algorithmic pseudocode is shown below.
```
Synthesize(inputs, outputs):
    plist := set of all terminals
    while(true):
        plist := grow(plist);
        plist := elimEquvalents(plist, inputs);
        forall( p in plist)
            if(isCorrect(p, inputs, outputs)): return p;
```

> The key steps in the algorithm are the `grow` operation, which uses the non-terminals in the grammar to construct new terms from all the terms in `plist`, and the `elimEquivalents` step, which eliminates all terms that are deemed to be redundant by virtue of being equivalent to other terms in the list. A key idea behind this algorithm is that the check of equivalence is not an real equivalence check, which would be expensive. Instead, the expressions are tested on the target inputs, and any two expression that produce the same outputs on these inputs are deemed equivalent, regardless of whether they are truly equivalent or not. This is what is referred to as "observational equivalence," the idea being that since we only care about the behavior of the synthesized program on the given inputs, any behavior difference on other inputs is irrelevant.

## 👨🏽‍💻 Project Description

Here, we implement the non-ML subset of BUSTLE, the algorithm proposed by [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381). That is, we implement bottom-up enumerative search for simple compound expressions, excluding conditionals, recursion, and loops. The implementation is generic and flexibly supports multiple target languages. Arithmetic and string manipulations are natively supported, defined in `arithmetic.py` and `string.py`, respectively.

To run the program, run `synthesis.py` with the following arguments:
```
usage: synthesis.py [-h] --domain {arithmetic,string} --examples {addition,subtraction,multiplication,division} [--max_weight MAX_WEIGHT]

Bottom-up enumerative synthesis in Python.

optional arguments:
  -h, --help            show this help message and exit
  --domain {arithmetic,string}
                        Domain of synthesis (either "arithmetic" or "string").
  --examples {addition,subtraction,multiplication,division}
                        Examples to synthesize program from. Must be a valid key in the "example_set" dictionary.
  --max-weight MAX_WEIGHT
                        Maximum weight of programs to consider before terminating search.
```

For example, to synthesize programs in the arithmetic domain from the addition input-output examples, run:
```
python synthesis.py --domain arithmetic --examples addition

Synthesis Log:
- Extracted 9 constants from examples.
- Searching level 2 with 9 primitives.

Synthesis Results:
- Program found in 0.0033s.
- Program: (x0 + x1)
- Program weight: 3
- Program return type: int
```

We could also try a more involved example in the string domain:
```
python synthesis.py --domain strings --example concatenate_3 --max-weight 5 

Synthesis Log:
- Extracted 13 constants from examples.
- Searching level 2 with 13 primitives.
- Searching level 3 with 79 primitives.
- Searching level 4 with 79 primitives.

Synthesis Results:
- Program found in 1.9864s.
- Program: Concat(x0, Concat(x1, x2))
- Program weight: 5
- Program return type: str
```

To add additional input-output examples, modify `examples.py`. Add a new key to the dictionary `example_set` and set the value to be a list of tuples.

## 🔎 Algorithmic Description

The most important data structure in this implementation is the abstract syntax tree (AST). The AST is a tree representation of a program, where each node is either a primitive or a compound expression. The AST is represented by the `OperatorNode` class in `abstract_syntax_tree.py`. My AST implementation includes functions to recursively evaluate the operator and its operands and also to generate a string representation of the program.

At program evaluation time, the AST is evaluated from the bottom up. That is, the operands are evaluated first, and then the operator is evaluated on the operands. This is implemented in the `evaluate` method of the `OperatorNode` class. In the case of integers, variable inputs are represented by the `IntegerVariable` class in `arithmetic.py`. When input is not `None`, input type checking and validation is performed by the `evaluate` function in this class.

The pseudocode for the bottom-up synthesis algorithm is reproduced below from [Odena *et al.* (2021)](https://arxiv.org/abs/2007.14381):

<img width="1494" alt="image" src="https://github.com/ayushnoori/program-synthesis/assets/43010710/117e7797-11af-4b72-b5f4-dda95eb2260f">

Note that we do not consider the lines colored in blue (*i.e.*, lines 4, 16, and 17). For details on machine learning-guided bottom-up search, please see the [BUSTLE paper](https://arxiv.org/abs/2007.14381).

## 🔮 Virtual Environment

To create a virtual environment, run:
```
conda deactivate
virtualenv synthesis_env
source synthesis_env/bin/activate
```

Then, install all required packages. To activate the virtual environment, run at the command line:
```
source setup.sh
```

To launch a Jupyter notebook, run:
```
source setup_jupyter.sh
```

## 🙏🏽 Acknowledgements

I thank [Tyler Holloway](mailto:tylerholloway@g.harvard.edu), teaching fellow in CS252R, for her guidance.

## 📫 Contact

Any questions? Please feel free to reach out to Ayush Noori at [anoori@college.harvard.edu](mailto:anoori@college.harvard.edu).

## 📖 References

1. Odena, A. *et al.* [BUSTLE: Bottom-Up Program Synthesis Through Learning-Guided Exploration.](https://arxiv.org/abs/2007.14381) in *9th International Conference on Learning Representations*; 2021 May 3-7; Austria.
