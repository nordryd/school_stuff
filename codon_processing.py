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
	startIndex : int
		The start index of the reading frame.
	stopIndex : int
		The stop index of the reading frame.
'''
class PossibleReadingFrame:
    def __init__( self, startIndex, stopIndex ):
        self.startIndex = startIndex
        self.stopIndex = stopIndex

'''
process_dna_strand - Take a DNA strand and find all the start and stop codons
					 to give a set possible reading frames.
Parameter:	Sequence to be analyzed.
Return:		The possible reading frames within the sequence.
'''
def process_dna_strand( sequence ):
    startIndexArr = []
    stopIndexArr= []
    possibleReadingFrameArr= []
    seq = sequence.upper()
    for i in range( 3 ):
        startIndexArr.append( [] )
        stopIndexArr.append( [] )
    for index in range( len( seq ) - 2 ):
        if seq[ index ] == "A" :
            triplet = seq[ index:index + 3 ]
            if triplet == "ATG" :
                startIndexArr[ index % 3 ].append( index )
                
        elif( seq[ index ] == "T" ):
            triplet = seq[ index:index + 3]
            if triplet == "TAA" or triplet == "TAG" or triplet == "TGA" :
                stopIndexArr[ index % 3 ].append( index )

    for frame in range( 3 ):
        if( len( startIndexArr[ frame ] ) != 0 
				and len( stopIndexArr[ frame ] ) != 0):
            startIndex = 0
            stopIndex = 0
            for i in range( len( startIndexArr[ frame ] ) +
                           len( stopIndexArr[ frame ] ) ):
                if( len( startIndexArr[ frame ] ) > startIndex 
						and len( stopIndexArr[ frame ] ) > stopIndex ):
                    
                    if( startIndexArr[ frame ][ startIndex ] 
							< stopIndexArr[ frame ][ stopIndex ] ):
                        possibleReadingFrameArr.append(
                            PossibleReadingFrame(
                                startIndexArr[ frame ][ startIndex ],
                                stopIndexArr[ frame ][ stopIndex ] ))
                        startIndex = startIndex + 1
                    else:
                        stopIndex = stopIndex + 1
    return possibleReadingFrameArr
