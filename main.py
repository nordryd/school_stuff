from sys import argv
from translate import translate
from translate import inverseTransverse
from codon_processing import process_dna_strand
from codon_processing import PossibleReadingFrame
from orf_interpretation import removeOptionsOfWrongSize
from orf_interpretation import getPromoterValue

class ORF:
    def __init__(self, possibleReadingFrame, promoterValue, sequence, dnaStrand, frame):
        self.possibleReadingFrame = possibleReadingFrame
        self.promoterValue = promoterValue
        self.sequence = sequence
        self.dnaStrand = dnaStrand
        self.frame = frame

def getBestOrf(orfWithValueArray):
    maxElement = orfWithValueArray[0]
    for element in orfWithValueArray:
        if element.promoterValue > maxElement.promoterValue :
            maxElement = element
    return maxElement
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
        orfWithValue1.append(ORF(elements,getPromoterValue(dna1[max(0,elements.startIndex - 200):max(0, elments.startIndex -50 + 1)]),dna1[elements.startIndex:elements.stopIndex+3], 1, elements.startIndex%3 + 1 ))
    for elements in possibleReadingFrameArr2:
        orfWithValue2.append(ORF(elements,getPromoterValue(dna2[max(0,elements.startIndex - 200):max(0, elements.startIndex -50 + 1)]),dna2[elements.startIndex:elements.stopIndex+3], 2, elements.startIndex%3 +1 ))
    final2 = []
    if(len(orfWithValue1) > 0):
        final2.append(getBestOrf(orfWithValue1))
    if(len(orfWithValue2) > 0):
        final2.append(getBestOrf(orfWithValue2))
    if(len(final2) > 0):
        bestOrf = getBestOrf(final2)
        print(bestOrf.dnaStrand, bestOrf.frame,bestOrf.possibleReadingFrame.startIndex, bestOrf.possibleReadingFrame.stopIndex,  bestOrf.sequence)
    else:
        print("no valid sequence was found")
