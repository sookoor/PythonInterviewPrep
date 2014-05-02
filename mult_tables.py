import sys
def mult_tables(max_val):
    for i in xrange(1, max_val + 1):
        for j in xrange(1, max_val + 1):
            sys.stdout.write("%4d" %(i * j))
        print ""

mult_tables(12)
