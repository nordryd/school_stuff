'''
codon_processing.py

Processer for a DNA strand to locate all the start and stop codons and return
a possible reading frame.

Carl Yarwood, Jacob Overton, Kai Ding
Last Edited 10/7/2018
'''

'''
Object to store a possible reading frame.
	
	Fields
	------
	start_index : int
		The start index of the reading frame.
	stop_index : int
		The stop index of the reading frame.
'''
class Possible_Reading_Frame:
    def __init__( self, start_index, stop_index ):
        self.start_index = start_index
        self.stop_index = stop_index

'''
process_dna_strand - Take a DNA strand and find all the start and stop codons
					 to give a set possible reading frames.
Parameter:	Sequence to be analyzed.
Return:		The possible reading frames within the sequence.
'''
def process_dna_strand( sequence ):
    start_index_arr = []
    stop_index_arr= []
    possible_reading_frame_arr= []
    seq = sequence.upper()
    for i in range( 3 ):
        start_index_arr.append( [] )
        stop_index_arr.append( [] )
    for index in range( len( seq ) - 2 ):
        if seq[ index ] == "A" :
            triplet = seq[ index:index + 3 ]
            if triplet == "ATG" :
                start_index_arr[ index % 3 ].append( index )
                
        elif( seq[ index ] == "T" ):
            triplet = seq[ index:index + 3]
            if triplet == "TAA" or triplet == "TAG" or triplet == "TGA" :
                stop_index_arr[ index % 3 ].append( index )

    for frame in range( 3 ):
        if( len( start_index_arr[ frame ] ) != 0 
				and len( stop_index_arr[ frame ] ) != 0):
            start_index = 0
            stop_index = 0
            for i in range( len( start_index_arr[ frame ] ) +
                           len( stop_index_arr[ frame ] ) ):
                if( len( start_index_arr[ frame ] ) > start_index 
						and len( stop_index_arr[ frame ] ) > stop_index ):
                    
                    if( start_index_arr[ frame ][ start_index ] 
							< stop_index_arr[ frame ][ stop_index ] ):
                        possible_reading_frame_arr.append(
                            Possible_Reading_Frame(
                                start_index_arr[ frame ][ start_index ],
                                stop_index_arr[ frame ][ stop_index ] ))
                        start_index = start_index + 1
                    else:
                        stop_index = stop_index + 1
    return possible_reading_frame_arr
