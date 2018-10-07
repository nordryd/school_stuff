'''
translate.py
Jon Beck
Last Edieted 10/7/2018

A program to read a DNA sense strand from a fasta file
and translate it into one-letter amino acid sequence.
Assumptions:
1. DNA is 5' to 3' and is a multiple of 3 in
length
2. fasta file has only one sequence
'''
from readfasta import readfasta
BasePairSwap = {"T" : "A",
                "A" : "T",
                "G" : "C",
                "C" : "G"}

def translate(fileName):
    dna = readfasta(fileName)[0][1]
    dna = dna.upper()
    return dna

def inverseTransverse(sequence):
    seq = sequence.upper()
    ivtv = ""
    for x in reversed(seq):
        ivtv += BasePairSwap[x]
    return ivtv
