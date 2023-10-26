# Bottom-Up Enumerative Synthesis

Completed for CS252R at the Harvard John A. Paulson School of Engineering and Applied Sciences, taught Fall 2023. 

## 🛠️ Inductive Program Synthesis

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

Here, we implement the non-ML subset of BUSTLE, the algorithm proposed by Odena *et al.* (2021). 

## 📖 References

1. Odena, A. *et al.* BUSTLE: Bottom-Up Program Synthesis Through Learning-Guided Exploration. in *9th International Conference on Learning Representations*; 2021 May 3-7; Austria.

