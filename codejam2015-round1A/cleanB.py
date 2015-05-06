#!/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/bin/python2.7

import sys

infile = sys.argv[1]
f = open(infile,'r')
for i,line in enumerate(f.readlines()):
    line = line.strip()
    if not line:
        break # avoids problems with blank lines at eof

    if line.split()[0] == 'Case':
        print line
f.close()
