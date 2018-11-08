from read_fasta import *
import numpy


def print_matrix( pairwise_matrix ):
    
    matrix = ''
    col_space_offset_f = 9 * " "
    col_space_offset_b = 10 * " "
    row_space_offset_single_digit = 4 * " "
    row_space_offset_double_digit = 3 * " "
    data_space_offset = 3 * " "
    column_titles = col_space_offset_f
    
    for i in range( 0, len( pairwise_matrix[ 0 ] ) ):
        
        if( i < 10 ):
            matrix_row = str( i ) + row_space_offset_single_digit
        else:
            matrix_row = str( i ) + row_space_offset_double_digit
            col_space_offset_b = 9 * " "

        column_titles = column_titles + str( i ) + col_space_offset_b
        
        for j in range( 0, len( pairwise_matrix[ 0 ] ) ):

            matrix_row = matrix_row + str(
                "{:.6f}".format( abs( pairwise_matrix[ i ][ j ] ) )
            ) + data_space_offset

        matrix = matrix + matrix_row + '\n'

    column_titles = column_titles + '\n'
    final_matrix = '\n' + column_titles + matrix
    print( final_matrix )

    
    
def is_transition( nucleotide_1, nucleotide_2 ):
    purines = [ 'A', 'G' ]
    pyrimidines = [ 'C', 'T' ]
    is_transition = ( nucleotide_1 in purines and nucleotide_2 in purines ) or (
        nucleotide_1 in pyrimidines and nucleotide_2 in pyrimidines )

    return is_transition



def K2P_metric( seq1, seq2 ):
    
    shorter_seq = seq1 if len( seq1 ) < len( seq2 ) else seq2

    num_transitions = 0
    num_transversions = 0
    
    for i in range( 0, len( shorter_seq ) ):
        if seq1[ i ] != seq2[ i ]:
            if is_transition( seq1[ i ], seq2[ i ] ):
                num_transitions += 1
            else:
                num_transversions += 1

    frac_sites_transition = num_transitions / len( shorter_seq )
    frac_sites_transversion = num_transversions / len( shorter_seq )

    transversion_sat_distance = 3
    if( frac_sites_transversion > 0.5 ):
        return transversion_sat_distance

    return -( 1 / 2 ) * numpy.log( 1 - 2 * frac_sites_transition -
                             frac_sites_transversion ) - ( 1 / 4 ) *numpy.log(
                                 1 - 2 * frac_sites_transversion )

def get_matrix():
    
    mt_dna_info = read_fasta( "mtDNA.fasta" )

    pairwise_matrix = numpy.zeros( (len( mt_dna_info ), len( mt_dna_info ) ) )

    for i in range( 0, len( mt_dna_info ) ):
        
        for j in range( 0, len( mt_dna_info ) ):
            
            this_distance = K2P_metric( mt_dna_info[ i ][ 1 ],
                                        mt_dna_info[ j ][ 1 ] ) 
            pairwise_matrix[ i ][ j ] = this_distance

    return pairwise_matrix

'''def main():
   print_matrix( get_matrix() )
   return 0
    
main()'''
