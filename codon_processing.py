import genetic_code

class Codon:
    def __init__(self, is_start, reading_frame, sequence):
        self.is_start = is_start
        self.reading_frame = reading_frame
        self.sequence = sequence
class PossibleReadingFrame:
    def __init__(self, startIndex, stopIndex):
        self.startIndex = startIndex
        self.stopIndex = stopIndex


def process_dna_strand(sequence):
    #codon_arr = []
    startIndexArr = []
    stopIndexArr= []
    possibleReadingFrameArr= []
    seq = sequence.upper()
    for i in range(3):
        startIndexArr.append([])
        stopIndexArr.append([])
    for index in range(len(seq) - 2):
        if(seq[index] == "A"):
            triplet = seq[index:index+3]
            if(triplet == "ATG"):
                startIndexArr[index%3].append(index)
                
        elif(seq[index] == "T"):
            triplet = seq[index:index+3]
            if(triplet == "TAA" or triplet == "TAG" or triplet == "TGA"):
                stopIndexArr[index%3].append(index)

    for frame in range(3):
        if(len(startIndexArr[frame]) != 0 and len(stopIndexArr[frame]) != 0):
            startIndex = 0
            stopIndex = 0
            for i in range(len(startIndexArr[frame]) + len(stopIndexArr[frame])):
                if( len(startIndexArr[frame]) > startIndex and len(stopIndexArr[frame])> stopIndex):
                    
                    if(startIndexArr[frame][startIndex] < stopIndexArr[frame][stopIndex]):
                        possibleReadingFrameArr.append(PossibleReadingFrame(startIndexArr[frame][startIndex], stopIndexArr[frame][stopIndex]))
                        startIndex = startIndex + 1
                    else:
                        stopIndex = stopIndex + 1
    return possibleReadingFrameArr

#dynamic programming, score based on how close the two strings are

#codons = process_dna_strand("TATGCGTTTA")
#for codon in codons:
#    print(codon.is_start, codon.reading_frame, codon.sequence)
