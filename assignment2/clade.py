
'''
A class to represent a single clade in a phylogenetic tree.
@author Jared Allen
@date November 4th, 2018
'''
class Clade:
    clade = []
    sub_clade1 = []
    sub_clade2 = []
    distance_bw_subclades = 0
    
    #clade1 and clade1 are lists
    def __init__( self, clade1, clade2 = None, distance = None ):
        '''
        constructs the clade object for a single taxa or two clades
        @param self the clade object
        @param clade1 the first subclade
        @param clade2 the second subclade
        @param distance the distance between the two subclades
        '''
        if( clade2 is None and distance is None):
            self.clade = clade1
        else:
            self.clade = [ clade1.get_clade(), clade2.get_clade() ]
            self.sub_clade1 = clade1
            self.sub_clade2 = clade2
            self.distance_bw_subclades = distance

    def get_clade( self ):
        '''returns the clade list itself'''
        return self.clade

    def get_distance( self ):
        '''returns the distance between the two subclades in this clade'''
        return self.distance_bw_subclades

    def get_sub_clades( self ):
        '''returns the subclades in a list'''
        sub_clades = [ self.sub_clade1, self.sub_clade2 ]
        return sub_clades
