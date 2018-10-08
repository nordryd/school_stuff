'''
main.py

Main file for the ORF program pipeline.

Carl Yarwood, Jacob Overton, Kai Ding
Last Edited 10/7/2018
'''
from sys import argv
from translate import translate
from translate import inverse_transverse
from codon_processing import process_dna_strand
from codon_processing import Possible_Reading_Frame
from orf_interpretation import remove_options_of_wrong_size
from orf_interpretation import get_promoter_value

'''
Object to store an open reading frame.
	
	Fields
	------
	possible_reading_frame : str
		The elements of a possible reading frame.
	promoter_value : int
		The value of the ORF's corresponding promoter value.
	sequence : str
		The sequence contained in the ORF.
	dna_strand : int [1, 2]
		Which strand of DNA this ORF resides on.
	frame : int
		The reading frame containing this ORF.
'''
class ORF:
    def __init__( self,
                  possible_reading_frame,
                  promoter_value,
                  sequence,
                  dna_strand,
                  frame ):
        self.possible_reading_frame = possible_reading_frame
        self.promoter_value = promoter_value
        self.sequence = sequence
        self.dna_strand = dna_strand
        self.frame = frame

'''
getBestOrf - Finds the best ORF, given an array of ORFs with identical
			 matching scores.
Parameter:	An array of ORFs, all earning the same matching score.
Return: 	The ORF with the best promoter value.
'''
def getBestOrf( orf_with_value_array ):
    max_element = []
    # our lowest possible value for a promoter match is -56
    best_value = -57
    for element in orf_with_value_array:
        if element.promoter_value > best_value :
            best_value = element.promoter_value
            max_element = []
            max_element.append( element )
        elif element.promoter_value == max_element[ 0 ].promoter_value:
            max_element.append( element )
    return max_element

'''
main - Main method for executing ORF pipeline.
Parameter:	A single .fasta file. Must be given via the command line.
Return:		The best ORF.
'''
def main():
    if( len( argv ) != 2 ):
        print( "Usage:  python3 main.py <fasta filename>.fasta" )
    else:
        dna1 = translate( argv[ 1 ] )
        dna2 = inverse_transverse( dna1 )
        possible_reading_frame_arr1 = process_dna_strand( dna1 )
        possible_reading_frame_arr2 = process_dna_strand( dna2 )
        possible_reading_frame_arr1 = (
			remove_options_of_wrong_size( possible_reading_frame_arr1 ))
        possible_reading_frame_arr2 = (
			remove_options_of_wrong_size( possible_reading_frame_arr2 ))

        orf_with_value_1 = []
        orf_with_value_2 = []
        for elements in possible_reading_frame_arr1:
            orf_with_value_1.append( ORF( elements,
                                     get_promoter_value( dna1[
                                        max( 0, elements.start_index - 200 ):
                                        max( 0, elements.start_index - 50 + 1
										)])
                                     ,dna1[
                                        elements.start_index:
                                        elements.stop_index + 3 ],
                                     1,
                                     elements.start_index % 3 + 1 ))
        for elements in possible_reading_frame_arr2:
            orf_with_value_2.append( ORF( elements,
                                     get_promoter_value(dna2[
                                         max(0,elements.start_index - 200):
                                         max(0, elements.start_index - 50 + 1
										 )]),
                                     dna2[
                                         elements.start_index:
                                         elements.stop_index + 3],
                                     2,
                                     elements.start_index % 3 + 1 ))
        finals = []
        if( len( orf_with_value_1 ) > 0 ):
            best_ORF1 = getBestOrf( orf_with_value_1 )
            for element in best_ORF1:
                finals.append( element )
        if( len( orf_with_value_2 ) > 0 ):
            best_ORF2 = getBestOrf( orf_with_value_2 )
            for element in best_ORF2:
                finals.append( element )
        if( len( finals ) > 0 ):
            bestOrf = getBestOrf( finals )
            frame = [ 0, 0, 0, 0, 0, 0 ]
            for element in bestOrf :
                if( element.possible_reading_frame.start_index % 3 == 0 
						and element.dna_strand == 1 ):
                    frame[ 0 ] = frame[ 0 ] + 1
                elif( element.possible_reading_frame.start_index % 3 == 1 
						and element.dna_strand == 1 ):
                    frame[ 1 ] = frame[ 1 ] + 1
                elif( element.possible_reading_frame.start_index % 3 == 2 
						and element.dna_strand == 1 ):
                    frame[ 2 ] = frame[ 2 ] + 1
                elif( element.possible_reading_frame.start_index % 3 == 0 
						and element.dna_strand == 2 ):
                    frame[ 3 ] = frame[ 3 ] + 1
                elif( element.possible_reading_frame.start_index % 3 == 1 
						and element.dna_strand == 2 ):
                    frame[ 4 ] = frame[ 4 ] + 1
                else:
                    frame[ 5 ] = frame[ 5 ] + 1
            best_frame = 0

            for index in range( 6 ):
                if frame[ index ] > frame[ best_frame ]:
                    best_frame = index
            best_frame = best_frame +1
            return best_frame
        else:
            return "no valid sequence was found"


print( main() )
