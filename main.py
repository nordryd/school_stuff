from translate import translate
from codon_processing import process_dna_strand
from codon_processing import PossibleReadingFrame

dna = translate('test.fasta')
possibleReadingFrameArr = process_dna_strand(dna)
