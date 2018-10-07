#orf orf orf orf orf
#TATA(A/T)A(A/T)(A/G)
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
def getPromoterValue( seq ):
    possibleValueArr = []
    for element in promoter:
        possibleValueArr.append( fuzzyMatch( element, seq ) )
    return max( possibleValueArr )

def fuzzyMatch( str1, str2 ):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    matchArr = numpy.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        matchArr[index][0] = index * gapPenalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [ ( matchArr[ row ][ col + 1 ] + gapPenalty ),
                                ( matchArr[ row + 1 ][ col ] + gapPenalty ),
                                ( ( matchArr[ row ][ col ] + matchReward ) if
                                ( workstr1[ row + 1 ] == workstr2[ col + 1 ] )
                                else ( matchArr[ row ][ col ] + matchPenalty ) ) ]
            matchArr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return max( matchArr [ len( workstr1 ) - 1 ] )

def removeOptionsOfWrongSize( possibleReadingFrameArr ):
    for element in reversed( possibleReadingFrameArr ):
        if( element.stopIndex + 2 - element.startIndex < 300 ):
            possibleReadingFrameArr.remove( element )
    return possibleReadingFrameArr
