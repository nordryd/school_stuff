from sys import argv
from translate import translate
from translate import inverseTransverse
from codon_processing import process_dna_strand
from codon_processing import PossibleReadingFrame
from orf_interpretation import removeOptionsOfWrongSize
from orf_interpretation import getPromoterValue

class ORF:
    def __init__(self,
                 possibleReadingFrame,
                 promoterValue,
                 sequence,
                 dnaStrand,
                 frame):
        self.possibleReadingFrame = possibleReadingFrame
        self.promoterValue = promoterValue
        self.sequence = sequence
        self.dnaStrand = dnaStrand
        self.frame = frame

def getBestOrf(orfWithValueArray):
    maxElement = []
    # our lowest possible value for a promoter match is -56
    bestValue = -57
    for element in orfWithValueArray:
        if element.promoterValue > bestValue :
            bestValue = element.promoterValue
            maxElement = []
            maxElement.append(element)
        elif element.promoterValue == maxElement[0].promoterValue:
            maxElement.append(element)
    return maxElement


def main():
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
            orfWithValue1.append(ORF(elements,
                                     getPromoterValue(dna1[
                                         max(0,elements.startIndex - 200):
                                         max(0, elements.startIndex - 50 + 1)])
                                     ,dna1[
                                         elements.startIndex:
                                         elements.stopIndex+3],
                                     1,
                                     elements.startIndex%3 + 1 ))
        for elements in possibleReadingFrameArr2:
            orfWithValue2.append(ORF(elements,
                                     getPromoterValue(dna2[
                                         max(0,elements.startIndex - 200):
                                         max(0, elements.startIndex - 50 + 1)]),
                                     dna2[
                                         elements.startIndex:
                                         elements.stopIndex + 3],
                                     2,
                                     elements.startIndex%3 + 1 ))
        finals = []
        if(len(orfWithValue1) > 0):
            bestORF1 = getBestOrf(orfWithValue1)
            for element in bestORF1:
                finals.append(element)
        if(len(orfWithValue2) > 0):
            bestORF2 = getBestOrf(orfWithValue2)
            for element in bestORF2:
                finals.append(element)
        if(len(finals) > 0):
            bestOrf = getBestOrf(finals)
            frame = [0,0,0,0,0,0]
            for element in bestOrf :
                if element.possibleReadingFrame.startIndex%3 == 0 and element.dnaStrand == 1 :
                    frame[0] = frame[0] + 1
                elif element.possibleReadingFrame.startIndex %3 == 1 and element.dnaStrand == 1:
                    frame[1] = frame[1] + 1
                elif element.possibleReadingFrame.startIndex %3 == 2 and element.dnaStrand == 1:
                    frame[2] = frame[2] + 1
                elif element.possibleReadingFrame.startIndex %3 == 0 and element.dnaStrand == 2:
                    frame[3] = frame[3] + 1
                elif element.possibleReadingFrame.startIndex %3 == 1 and element.dnaStrand == 2:
                    frame[4] = frame[4] + 1
                else:
                    frame[5] = frame[5] + 1
            bestframe = 0

            for index in range(6):
                if frame[index] > frame[bestframe]:
                    bestframe = index
            bestframe = bestframe +1
            return bestframe
        else:
            return "no valid sequence was found"


print(main())
