'''
translate.py

A program to read a DNA sense strand from a fasta file
and translate it into one-letter amino acid sequence.
Assumptions:
1. DNA is 5' to 3' and is a multiple of 3 in
length
2. fasta file has only one sequence

Jon Beck
Last Edited 10/7/2018 by Carl Yarwood, Jacob Overton, and Kai Ding
'''
from readfasta import readfasta
BasePairSwap = {"T" : "A",
                "A" : "T",
                "G" : "C",
                "C" : "G"}

'''
translate - Read a .fasta file and convert it into a one-letter amino acid
			sequence.
Parameter:	Filename of a .fasta file.
Return:		A one-letter amino acid sequence. All letters will be UPPERCASE.
'''
def translate( fileName ):
    dna = readfasta( fileName )[ 0 ][ 1 ]
    dna = dna.upper()
    return dna

'''
inverseTranverse - Inverts a given sequence based on DNA base pairs.
Parameter:	DNA sequence to be inverted. Must be DNA.
Return:		The inverted DNA sequence.
'''
def inverseTransverse( sequence ):
    seq = sequence.upper()
    ivtv = ""
    for x in reversed( seq ):
        ivtv += BasePairSwap[ x ]
    return ivtv
