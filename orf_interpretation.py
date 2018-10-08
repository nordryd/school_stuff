'''
orf_interpretation.py

Handles promoter matching using dynamic programming.

Carl Yarwood, Jacob Overton, Kai Ding
Last Edited 10/7/2018
'''
import numpy
from codon_processing import Possible_Reading_Frame

promoter = ["TATAAAAA",
            "TATATAAA",
            "TATAAATA",
            "TATAAAAG",
            "TATATATA",
            "TATATAAG",
            "TATAAATG",
            "TATATATG"]
gap_penalty = -7
match_penalty = -4
match_reward = 5

'''
get_promoter_value - Get the promoter value for a given sequence.
Parameter:	Sequence to find a matching promoter in.
Return:		The sequence with the highest promoter value.
'''
def get_promoter_value( seq ):
    possible_value_arr = []
    for element in promoter:
        possible_value_arr.append( fuzzy_match( element, seq ) )
    return max( possible_value_arr )

'''
fuzzy_match - Use dynamic programming to match a given sequence and promoter
			 string together.
Parameters:	A sequence and the promoter sequence to compare it to.
Return:		The highest score in the matrix.
'''
def fuzzy_match( str1, str2 ):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    match_arr = numpy.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        match_arr[ index ][ 0 ] = index * gap_penalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [( match_arr[ row ][ col + 1 ] + gap_penalty ),
                               ( match_arr[ row + 1 ][ col ] + gap_penalty ),
                               ( ( match_arr[ row ][ col ] + match_reward )
							   if
                               ( workstr1[ row + 1 ] == workstr2[ col + 1 ])
                               else( match_arr[ row ][ col ] + match_penalty
							   ))]
            match_arr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return max( match_arr [ len( workstr1 ) - 1 ] )

'''
remove_options_of_wrong_size - Filter elements in a reading frame of the
						   incorrect size.
Parameter:	Reading frame to be filtered.
Return:		Reading frame with all the results being the correct size.
'''
def remove_options_of_wrong_size( possible_reading_frame_arr ):
    for element in reversed( possible_reading_frame_arr ):
        if( element.stop_index + 2 - element.start_index < 300 ):
            possible_reading_frame_arr.remove( element )
    return possible_reading_frame_arr
