#!/usr/bin/python

import sys

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
    l = line.strip().split()
    
    for i in range(1,len(l)):
        
        # output goes to STDOUT (stream data that the program writes)
        print "%s\t%d" %( [l[i-1],l[i]], 1 )