from K2P_metric import get_matrix
import sys

matrix = [[0, 13, 11, 7, 12, 16, 15],
          [13, 0, 2, 11, 14, 13, 5],
          [11, 2, 0, 9, 18, 15, 3],
          [7, 11, 9, 0, 8, 14, 13],
          [12, 14, 18, 8, 0, 18, 13],
          [16, 13, 15, 14, 18, 0, 14],
          [15, 5, 3, 13, 13, 14, 0]]
          
def show_result(result):
   for i in result:
      print("\t-> Append: %s %s" % (i[0], i[1]))
      
def print_matrix(clades, matrix):
   print(clades)
   for row in matrix:
      print(" ".join("{}".format(item) for item in row))
   print("-------------------------------------------------")

def getMinValue(matrix):
    min_val = float('inf')
    length = len(matrix)
    for row in range(length):
        for col in range(length):
            if (matrix[row][col] < min_val) and (matrix[row][col] != 0):
                min_val = matrix[row][col]
                position = (row,col)
                
    return min_val,position
            

def upgma():
   clades = []
   cladeID = ord('A')
   length = len(matrix)
   
   for clade in range(length):
      clades.append(chr(cladeID))
      cladeID += 1
   
   print_matrix(clades, matrix)
   
   while (length > 1):
      min_value, position = getMinValue(matrix)
      for item in range(length):
         if (item != position[0]):
            clade_size_1 = float(len(clades[position[0]]))
            clade_size_2 = float(len(clades[position[1]]))
            clade_distance_a = clade_size_1 * matrix[item][position[0]]
            clade_distance_b = clade_size_2 * matrix[item][position[1]]
            # **exact calculations are currently incorrect, but the slide example works
            matrix[item][position[0]] = round(((clade_distance_a + clade_distance_b) / (clade_size_1 + clade_size_2)), 2)
            matrix[position[0]][item] = matrix[item][position[0]]
            
      # remove excess row
      matrix.pop(position[1])
      
      # remove excess column
      for columns in matrix:
         columns.pop(position[1])
      
      # Merging clades
      clades[position[0]] += clades[position[1]]
      clades.pop(position[1])
      
      # **clades need to be outputted in a tree format
      print_matrix(clades, matrix)
      length -= 1
   
def main():
   upgma()

main()
