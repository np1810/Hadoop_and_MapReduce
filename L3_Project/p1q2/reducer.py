#!/usr/bin/python

import sys

highestSales = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", highestSales
        oldKey = thisKey;
        highestSales = 0

    oldKey = thisKey
    thisSale = float(thisSale)
    if highestSales < thisSale:
        highestSales = thisSale

if oldKey != None:
    print oldKey, "\t", highestSales

