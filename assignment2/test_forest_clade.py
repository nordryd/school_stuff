from clade import *
from forest import *

def main():

    forest1 = Forest()
    
    clade1 = Clade( Clade( 1 ), Clade( 2 ), 10 )
    forest1.new_clade( clade1, 0 )

    print( forest1.get_trees() )
    print( forest1.get_num_clades () )
    
    print( "\n" )
    
    clade2 = Clade( clade1, Clade( 3 ), 20 )
    forest1.new_clade( clade2, 0 )
    
    print( forest1.get_trees() )
    print( forest1.get_num_clades () )
    
    print( "\n" )
    
    clade3 = Clade( Clade( 4 ), clade2, 15 )
    forest1.new_clade( clade3, 0 )

    print( forest1.get_trees() )
    print( forest1.get_num_clades () )
    
    print( "\n" )
    
    clade4 = Clade( Clade( 5 ), Clade( 6 ), 13 )
    forest1.new_clade( clade4, 1 )

    print( forest1.get_trees() )
    print( forest1.get_num_clades () )
   
    print( "\n" )
    
    clade5 = Clade( clade4, clade3, 12 )
    forest1.join_trees( clade4, clade3, 17 )

    print( forest1.get_trees() )
    print( forest1.get_num_clades () )
    
    print( "\n" )

    forest1.print_forest()

