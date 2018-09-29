import genetic_code

class Codon:
    def __init__(self, is_start, reading_frame, sequence):
        self.is_start = is_start
        self.reading_frame = reading_frame
        self.sequence = sequence

def process_dna_strand(sequence):
    codon_arr = []
    seq = sequence.upper()
    found_start_codon = False

    for index in range(len(seq) - 2):
        if(seq[index] == "A" and found_start_codon == False):
            triplet = seq[index:index+3]
            if(triplet == "ATG"):
                codon_arr.append(Codon(not found_start_codon, index % 3, triplet))
                found_start_codon = not found_start_codon
        elif(seq[index] == "T" and found_start_codon == True):
            print("end codon found")
            found_start_codon = not found_start_codon

    return codon_arr


codons = process_dna_strand("TATGCGTTTA")
for codon in codons:
    print(codon.is_start, codon.reading_frame, codon.sequence)
