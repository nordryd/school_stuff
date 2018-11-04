import random
import readfasta

def main():
    my_sequences = ["here is my string", "hure is mu string"]
    bootstrap(my_sequences)
    find_lengths()

'''
Bootstrap takes a list of sequences (strings of the same size) and 
randomly samples sites to produce trees and returns the 
confidence of each clade.
parameters-list of sequences
return-newick format of a tree with confidence of each clade
'''
def bootstrap( old_sequences ): #may also include tree as param
    #Create a list of empty strings for the new sequences
    new_sequences = []
    for i in range(0, len(old_sequences)):
            new_sequences.append("")
    #Fill new_strings with random indexes
    for i in range(0,len(old_sequences[0])):
        rand = random.randint(0, len(old_sequences[0]) - 1)
        for j in range(0, len(old_sequences)):
            new_sequences[j] = new_sequences[j] + old_sequences[j][rand]
    '''
    clades = {}
    for i in range(0, 1000):
        find_tree(new_sequences)
        #Add all found clades to clades dictionary where key is the clade and
        #value is the number of times it was found
    return tree w/ values from clades dictionary
    '''
def find_lengths():
    seqs = readfasta.readfasta("mt_homo_dna.fasta.txt")
    for i in range(0, len(seqs)):
        print(len(seqs[i][1]))
main()
