
'''
A class to represent the phylogenetic forest during
UPGMA tree construction
@author Jared Allen
@date November 4th, 2018
'''

from clade import *

class Forest:
    trees = []
    clades = []

    
    def __init__( self, trees = None, distances = None, num_clades = None ):
        if( trees is not None and distances is not None and num_clades is not
            None ):
            self.trees = trees
            self.distances = distances
            self.num_clades = num_clades

    #tree num is determined by upgma matrix; if two OTUs are joined into new
    #clade, we have a new tree.
    def new_clade(self, clade, tree_num ):
        '''
        inserts a clade into the forest.
        @param self the forest object
        @param clade the clade to be inserted
        @param tree_num the index of the tree that the clade will insert into
        '''
        self.clades.append( clade )
        if( ( tree_num + 1 ) > len( self.trees ) ):
            
            self.trees.append( [] )
            self.trees[ tree_num ] = clade.get_clade()
            
        else:
            
            self.trees[ tree_num ] = clade.get_clade() 
           

    #if both the row and the column index is a clade of more than 1 OTU, we must
    #join the two trees that represent those clades. These clades must be trees
    #at this point.
    def join_trees(self, clade1, clade2, distance ):
        '''
        Joins two trees together into a single clade.
        @param self the forest object
        @param clade1 the first clade to be joined
        @param clade2 the second clade to be joined
        '''
        tree_num_1 = self.trees.index( clade1.get_clade() )
        tree_num_2 = self.trees.index( clade2.get_clade() )
        
        self.clades.append( Clade( Clade( self.trees[ tree_num_1 ] ),
                                   Clade( self.trees[ tree_num_2 ] ), distance ) )

        self.trees[ tree_num_1 ] = [ self.trees[ tree_num_1 ], self.trees[
            tree_num_2 ] ]
        
        self.trees[ tree_num_2 ] = []

        new_trees = []
        for i in range( 0, len( self.trees ) ):
            
            if( len( self.trees[ i ] ) > 0 ):
                new_trees.append( self.trees[ i ] )

        self.trees = new_trees

        
    def print_forest( self ):

        for clade in self.clades:
            print( clade.get_clade(), clade.get_distance() )

        print("Here is the Newick format for the trees: " )
        for tree in self.trees:
            print( tree )                  
                        

    #here are the accessors
    def get_trees( self ):
        '''returns the trees in the forest'''
        return self.trees

    def get_num_clades( self ):
        '''returns the number of clades'''
        return len( self.clades )
