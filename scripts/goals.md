## M01

* Know the definitions of and notation for **set**, **subset**, **power set**, **Cartesian product**, and the set operations **union**, **intersection**, **difference**, and **complement**.
* Be able to state $|\mathcal{P}(A)|$ and $|A \times B|$ without writing the sets out.
* Know the definitions of **domain**, **codomain**, and **range** of a function, and be able to say whether a given assignment is a well-defined function.
* Be able to prove a simple set identity (e.g. one of De Morgan's laws) by an element-wise argument.
* Know how to read an **inductive definition** of a structure, and be able to prove a claim about all such structures by **structural induction**, stating the base case and inductive hypothesis explicitly.

## M02

* Know the definitions of and notation for **alphabet**, **symbol**, **string**, **length**, the empty string $\varepsilon$, **concatenation**, $\Sigma^*$, and **language**.
* Know the difference between $\varepsilon$, $\varnothing$, and $\{\varepsilon\}$.
* Know the formal definition of a **DFA** as a 5-tuple, be able to translate between the 5-tuple and the state diagram, and be able to trace a machine's computation on a given input string.
* Know what it means for a DFA to **accept** a string, and know the definition of $L(M)$, the language **recognized** by a machine $M$.
* Be able to construct a DFA that recognizes a simple language over a small alphabet.
* Be able to decide whether a given DFA recognizes the empty language.

## M04

* Be able to design a DFA for a language described in English, and say what each state remembers about the input read so far.
* Know the definition of a **regular language**, and know what it means for a class of languages to be **closed** under an operation.
* Be able to carry out the **product construction** on two DFAs: its state set, start state, transition function, and accept states.
* Be able to prove that the regular languages are closed under **union**, **intersection**, and **complement**.
* Be able to decide whether two DFAs are **equivalent** by building a DFA for their **symmetric difference** and testing it for emptiness, and to recover a shortest **distinguishing string** from the same search.

## M05

* Know how an **NFA** differs from a DFA.
* Be able to trace the computation and acceptance/rejection of an NFA on a given input string.
* Know the formal definition of an NFA as a 5-tuple, and the formal definition of its computation and acceptance.
* Be able to design an NFA for regular languages described in English or set notation.

## M06

* Be able to state the theorem that every NFA has an equivalent DFA, and the corollary that a language is regular if and only if some NFA recognizes it.
* Know the definition of $E(R)$, the **$\varepsilon$-closure** of a set of states, and be able to compute it for a small NFA.
* Be able to carry out the **subset construction** on a small NFA, and justify its correctness.
* Know that the size of the DFA may be exponential in the size of the NFA, and be able to give a language that results in this kind of blowup.
* Understand the role of $\varnothing$ in the subset construction and the resulting DFA.

## M07

* Know the definitions of the **regular operations** on languages — **union**, **concatenation**, and **star** — and know that $\varepsilon \in A^*$ for every language $A$, including $A = \varnothing$.
* Be able to prove using NFA constructions that the regular languages are closed under union, concatenation, and star.
* Know the formal, inductive definition of a **regular expression**, including $\varnothing$ and $\varepsilon$ as base cases, and know the difference between the expressions $\varnothing$ and $\varepsilon$.
* Be able to describe the language denoted by a given regular expression, and to write a regular expression for a language described in English.
* Know the **operator precedence** conventions for regular expressions (star, then concatenation, then union) and be able to simplify an expression using basic the identities like $R \cup \varnothing = R$, $R \circ \varepsilon = R$, and $\varnothing^* = \{\varepsilon\}$.

## M08

* Know the statement of **Kleene's theorem** - a language is regular if and only if some regular expression describes it - and that it is proved as two lemmas, one per direction.
* Be able to give the NFA for each base case of the definition of a regular expression — $a$, $\varepsilon$, and $\varnothing$.
* Be able to carry out the **union**, **concatenation**, and **star** constructions on NFA fragments, and describe what each added $\varepsilon$-arrow is for.
* Be able to convert a small regular expression to an NFA using the **Thompson construction**.
* Know that the construction is compositional and does **not** produce the smallest NFA for the language.

## M09

* Know what a **GNFA** is and how it differs from an NFA.
* Know the **special form** a GNFA must be in for the state elimination algorithm, and be able to put a given DFA into it.
* Be able to carry out **state elimination**: rip a state $q_{\text{rip}}$ and relabel each remaining arrow $q_i \to q_j$ as $(R_1)(R_2)^*(R_3) \cup (R_4)$, and describe what each of the four expressions is.
* Be able to say why ripping a state preserves the language, and why the procedure terminates.
* Be able to convert a small DFA to a regular expression describing its language, and say how this direction, together with module 8's, closes Kleene's theorem.

## M10

* Know the definition of the **indistinguishability** relation $x \equiv_L y$, and recognize that it is an equivalence relation that partitions $\Sigma^*$ into classes of strings.
* Be able to decide whether two strings are **distinguishable** with respect to a language, and give a distinguishing suffix $z$ when they are.
* Know the statement of the **Myhill-Nerode theorem** in the form this module uses it: the minimum number of states in a DFA recognizing $L$ equals the number of equivalence classes of $\equiv_L$.
* Be able to use the equivalence classes of a regular language to build a **minimal DFA** using those classes as states.
* Be able to run **Moore's table-filling algorithm** on a DFA with an unreachable state and a dead state, and say what each pass established.

## M11

* Know the statement of the **pumping lemma**, including all three conditions, and know what the **pumping length** $p$ is.
* Be able to give an informal intuitive argument for the lemma, and explain where each of the three conditions comes from.
* Be able to prove a language **nonregular** with the lemma.
* Be able to also prove a language nonregular using a Myhill-Nerode distinguishability argument.

## M12

* Know the formal definition of a **context-free grammar** as a 4-tuple $(V, \Sigma, R, S)$, the meaning of **yields** ($\Rightarrow$) and **derives** ($\stackrel{*}{\Rightarrow}$), and the definition of $L(G)$, the language **generated** by a grammar $G$.
* Be able to give a **derivation** and a **parse tree** for a string in the language of a given grammar, and know what makes a derivation **leftmost**.
* Be able to describe the language generated by a small grammar, and to write a grammar for a language described in English or set notation, or recognized by a given DFA.
* Know the definition of an **ambiguous** grammar, and be able to show that a grammar is ambiguous by giving a string with two different parse trees or two different left-most derivations.
* Know how a grammar for arithmetic expressions can be layered to encode operator **precedence** and remove ambiguity.

## M13

* Know the definition of **Chomsky normal form**, including the restrictions on the start variable and the one $\varepsilon$-rule it allows.
* Know that every context-free language is generated by some grammar in Chomsky normal form.
* Be able to remove **$\varepsilon$-rules** and **unit rules** from a small grammar without changing the language it generates.
* Be able to convert a small grammar to Chomsky normal form.
* Be able to prove that in a grammar in Chomsky normal form, every derivation of a string of length $n \ge 1$ takes exactly $2n - 1$ steps.

## M14

* Know how a **pushdown automaton (PDA)** extends an NFA with a **stack**, and what it means to **push** and **pop**.
* Know the formal definition of a PDA as a 6-tuple, including the **stack alphabet** $\Gamma$ and the domain and range of $\delta$, and be able to read a transition labeled $a, b \to c$, including when any of $a$, $b$, $c$ is $\varepsilon$.
* Be able to trace a PDA's computation on an input string, tracking its state and stack contents, and decide whether it accepts.
* Be able to design a PDA for a simple non-regular language, using a bottom-of-stack marker `$` to test for an empty stack.
* Be able to use **nondeterminism** in a PDA design, e.g. to guess the midpoint of a string in $\{ww^R\}$.

## M15

* Be able to state the theorem that CFGs and PDAs are equivalent.
* Be able to convert a small CFG to an equivalent PDA, and trace it on an input string to show how it uses its stack to simulate a **leftmost derivation**.
* Know the normal form a PDA is put into for the PDA-to-CFG direction, and what strings the variable $A_{pq}$ generates.
* Be able to explain why every regular language is context free.

## M16

* Know the statement of the **pumping lemma for context-free languages**, including all three conditions, and how it differs from the pumping lemma for regular languages.
* Be able to give an informal argument for the lemma in terms of parse trees, and explain where each of the three conditions comes from.
* Be able to prove a language **not context free** with the lemma.
* Be able to give a language that is context free but not regular, and one that is not context free, and justify each claim.

## M17

* Be able to prove that the context-free languages are closed under **union**, **concatenation**, and **star** by building a grammar from grammars for the pieces.
* Be able to show that the context-free languages are **not** closed under **intersection** or **complement**.
* Know that the intersection of a context-free language with a regular language is context free, and be able to use that fact to prove a language is not context free.
* Know that **membership** and **emptiness** are decidable for CFGs, and be able to decide whether a CFG generates any strings at all.
* Know that, unlike for DFAs, no algorithm can decide whether two CFGs are **equivalent**, and why an approach like the one we used for DFAs fails.
