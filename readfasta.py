'''
readfasta.py

Two routines to use to read a fasta file.

Jon Beck
Last Edited 8/20/18
'''

'''
parseHeader - split out the label from the header line
Parameter: a string starting with ">" and ending without a newline
Return: 
  1. the first item in the string, after the ">", up to the first space
'''
def parse_header_line( line ):
    label = line[ 1: ].split(' ')[ 0 ]
    return label

'''
readfasta - the subroutine that reads the fasta file
Parameter: a filename that must be in fasta format.  The file is
assumed to have:
1. the first line a header line
2. arbitrary blank lines
3. every line (especially including the last) is terminated by a newline
   terminator (enter key)
4. no line has only spaces on it

Return: a list of lists. Each inner list will have two elements:
1. the sequence identifier, i.e., the characters between the leading ">"
   and the first space
2. the sequence, a single string of all the letters with no line terminators
'''
def readfasta( filename ):
    result_list = []
    with open( filename, 'r' ) as in_file:

        # process the first line, which must be a header line
        line = in_file.readline()
        header_line = line.rstrip()
        label = parse_header_line( header_line )

        # initialize the sequence accumulator
        sequence = ''

        # process all the rest of the lines in the file
        for line in in_file:
            line = line.rstrip()

            # ignore blank lines
            if line != '':

                # if it's a header line, finish the previous sequence
                # and start a new one
                if line[0] == '>':
                    result_list.append( [ label, sequence ] )

                    label = parse_header_line( line )
                    sequence = ''
            
                    # if we're here, we must be in letters of the sequence
                else:
                    sequence += line
            
    # we're done, so clean up, terminate the last sequence, and return
    result_list.append( [ label, sequence ] )
    return result_list

