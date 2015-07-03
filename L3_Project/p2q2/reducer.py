#!/usr/bin/python

import sys

totalHits = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    if oldKey and oldKey != data_mapped[0]:
        print totalHits, "\t", oldKey        
        oldKey = data_mapped[0];
        totalHits = 0

    oldKey = data_mapped[0]
    totalHits += 1

if oldKey != None:
    print totalHits, "\t", oldKey

