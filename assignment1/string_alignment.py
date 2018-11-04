class ScoreParam:
    def __init__(self, match, mismatch, gap, gap_start=0):
        self.gap_start = gap_start
        self.gap = gap
        self.match = match
        self.mismatch = mismatch

    def matchchar(self, a,b):
        assert len(a) == len(b) == 1
        if a==b:
            return self.match
        else:
            return self.mismatch

    def __str__(self):
        return "match = %d; mismatch = %d; gap_start = %d; gap_extend = %d" % (
                self.match, self.mismatch, self.gap_start, self.gap
        )

def matrix(col, row):
    #create the memo table
    return [[0]*row for i in range(col)]

def print_matrix(x, y, A):
    # decide whether there is a 0th row/column
    if len(x) == len(A):
        print "%5s" % (" "),
    else:
        print "%5s %5s" % (" ","*"),
        y = "*" + y

    # print the top row
    for c in x:
        print "%5s" % (c),
    print

    for j in xrange(len(A[0])):
        print "%5s" % (y[j]),
        for i in xrange(len(A)):
            print "%5.0f" % (A[i][j]),
        print

def local_align(x, y, score=ScoreParam(10, -5, -7)):
    # create a zero-filled matrix
    A = matrix(len(x) + 1, len(y) + 1)

    best = 0
    optloc = (0,0)

    # fill in A in the right order
    for i in xrange(1, len(x)+1):
        for j in xrange(1, len(y)+1):

            # the local alignment recurrance rule:
            A[i][j] = max(
               A[i][j-1] + score.gap,
               A[i-1][j] + score.gap,
               A[i-1][j-1] + score.matchchar(x[i-1], y[j-1]),
               0
            )

            # track the cell with the largest score
            if A[i][j] >= best:
                best = A[i][j]
                optloc = (i,j)

    print "Scoring:", str(score)
    print "A matrix ="
    print_matrix(x, y, A)
    print "Optimal Score =", best
    print "Max location in matrix =", optloc
    # return the opt score and the best location
    return best, optloc


local_align("agt", "aagc", ScoreParam(gap=-2, match=1, mismatch=-1))