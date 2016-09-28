Tautology Verifier

A tautology verifier is a program that takes a "propositional statement" and verifies the statement
is a "tautology" or not.

Steps to run:

1> Clone the code locally.
2> Run the command --
      python tautology_verifier.py

sample input : "(!A | (A & A)), (!a | (b & !a)), (!a | a), ((a & (!b | b)) | (!a & (!b | b)))"
output: True
        False