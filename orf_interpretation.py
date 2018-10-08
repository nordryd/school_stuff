'''
orf_interpretation.py

Handles promoter matching using dynamic programming.

Carl Yarwood, Jacob Overton, Kai Ding
Last Edited 10/7/2018
'''
import numpy
from codon_processing import PossibleReadingFrame

promoter = ["TATAAAAA",
            "TATATAAA",
            "TATAAATA",
            "TATAAAAG",
            "TATATATA",
            "TATATAAG",
            "TATAAATG",
            "TATATATG"]
gapPenalty = -7
matchPenalty = -4
matchReward = 5

'''
getPromoterValue - Get the promoter value for a given sequence.
Parameter:	Sequence to find a matching promoter in.
Return:		The sequence with the highest promoter value.
'''
def getPromoterValue( seq ):
    possibleValueArr = []
    for element in promoter:
        possibleValueArr.append( fuzzyMatch( element, seq ) )
    return max( possibleValueArr )

'''
fuzzyMatch - Use dynamic programming to match a given sequence and promoter
			 string together.
Parameters:	A sequence and the promoter sequence to compare it to.
Return:		The highest score in the matrix.
'''
def fuzzyMatch( str1, str2 ):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    matchArr = numpy.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        matchArr[ index ][ 0 ] = index * gapPenalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [ ( matchArr[ row ][ col + 1 ] + gapPenalty ),
                                ( matchArr[ row + 1 ][ col ] + gapPenalty ),
                                ( ( matchArr[ row ][ col ] + matchReward ) if
                                ( workstr1[ row + 1 ] == workstr2[ col + 1 ])
                                else( matchArr[ row ][ col ] + matchPenalty )
								)]
            matchArr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return max( matchArr [ len( workstr1 ) - 1 ] )

'''
removeOptionsOfWrongSize - Filter elements in a reading frame of the
						   incorrect size.
Parameter:	Reading frame to be filtered.
Return:		Reading frame with all the results being the correct size.
'''
def removeOptionsOfWrongSize( possibleReadingFrameArr ):
    for element in reversed( possibleReadingFrameArr ):
        if( element.stopIndex + 2 - element.startIndex < 300 ):
            possibleReadingFrameArr.remove( element )
    return possibleReadingFrameArr
