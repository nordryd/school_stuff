from sys import argv
from translate import translate
from translate import inverseTransverse
from codon_processing import process_dna_strand
from codon_processing import PossibleReadingFrame
from orf_interpretation import removeOptionsOfWrongSize
from orf_interpretation import getPromoterValue

class ORF:
    def __init__(self, possibleReadingFrame, promoterValue, sequence):
        self.possibleReadingFrame = possibleReadingFrame
        self.promoterValue = promoterValue
        self.sequence = sequence

if(len(argv) != 2):
    print("Usage:  python3 main.py <fasta filename>.fasta")
else:
    dna1 = translate(argv[1])
    dna2 = inverseTransverse(dna1)
    possibleReadingFrameArr1 = process_dna_strand(dna1)
    possibleReadingFrameArr2 = process_dna_strand(dna2)
    possibleReadingFrameArr1 = removeOptionsOfWrongSize(possibleReadingFrameArr1)
    possibleReadingFrameArr2 = removeOptionsOfWrongSize(possibleReadingFrameArr2)
    orfWithValue1 = []
    orfWithValue2 = []
    for elements in possibleReadingFrameArr1:
        orfWithValue1.append(ORF(element,getPromoterValue(dna1[max(0,element.startIndex - 200):max(0, elment.startIndex -50 + 1)]),dna1[element.startIndex:element.stopIndex+3] ))
    for elements in possibleReadingFrameArr2:
        orfWithValue2.append(ORF(element,getPromoterValue(dna2[max(0,element.startIndex - 200):max(0, elment.startIndex -50 + 1)]),dna2[element.startIndex:element.stopIndex+3] ))
    final2 = []
    final2.append(getBestOrf(orfWithValue1))
    final2.append(getBestOrf(orfWithValue2))
    bestOrf = getBestOrf(final2)
    print(bestOrf.sequence)
    
    

def getBestOrf(orfWithValueArray):
    max = orfWithValueArray[0]
    for element in orfWithValueArray:
        if element.promoterValue > max.promoterValue :
            max = element
    return max
