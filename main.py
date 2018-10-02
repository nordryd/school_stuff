from sys import argv
from translate import translate
from translate import inverseTransverse
from codon_processing import process_dna_strand
from codon_processing import PossibleReadingFrame
from codon_processing import deleteDuplicates
if(len(argv) != 2):
    print("Usage:  python3 main.py <fasta filename>.fasta")
else:
    dna1 = translate(argv[1])
    dna2 = inverseTransverse(dna1)
    possibleReadingFrameArr1 = process_dna_strand(dna1)
    possibleReadingFrameArr1 = deleteDuplicates(possibleReadingFrameArr1)
    possibleReadingFrameArr2 = process_dna_strand(dna2)
    possibleReadingFrameArr2 = deleteDuplicates(possibleReadingFrameArr2)
