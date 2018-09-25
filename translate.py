'''
translate.py
Jon Beck

A program to read a DNA sense strand from a fasta file
and translate it into one-letter amino acid sequence.
Assumptions:
1. DNA is 5' to 3' and is a multiple of 3 in
length
2. fasta file has only one sequence
'''
from readfasta import readfasta
#from genetic_code import code

def translate(fileName):
    dna = readfasta(fileName)[0][1]
    dna = dna.upper()
    #rna = dna.replace('T', 'U')
    
    #aa_sequence = ''
    
    #for i in range(0, len(rna), 3):
        #codon = rna[i:i + 3]
        #aa = code[codon]
        #aa_sequence += aa
        
    #print(aa_sequence)
    return dna

