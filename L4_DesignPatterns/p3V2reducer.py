#!/usr/bin/python

import sys

def printIndex():
    nodeIDs.sort()
    try:
        print oldKey, "\t", wc, "\t", nodeIDs
    except IOError as e:
        print oldKey, "\tError"

wc = 0
nodeIDs = []
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisNode = data_mapped

    if oldKey and oldKey != thisKey:
        printIndex()
        nodeIDs = []
        wc = 0

    oldKey = thisKey
    wc += 1
    n = int(thisNode)
    if not n in nodeIDs:
        nodeIDs.append(n)

if oldKey != None:
    printIndex()

