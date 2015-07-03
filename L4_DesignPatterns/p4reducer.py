#!/usr/bin/python

import sys

salesCount = 0
salesTotal = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", (salesTotal/salesCount)
        oldKey = thisKey;
        salesTotal = 0
        salesCount = 0

    oldKey = thisKey
    salesTotal += float(thisSale)
    salesCount += 1

if oldKey != None:
    print oldKey, "\t", (salesTotal/salesCount)

