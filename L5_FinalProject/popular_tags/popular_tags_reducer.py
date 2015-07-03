#!/usr/bin/python
import sys
from operator import itemgetter

def adder(tagN,tagW):					# Adder Function which maintains Top N list
    l = len(topNTags)
    if len(topNTags) == None:l = 0
    if l < N or topNTags[N-1][1] < totalWeight:
        if l == N:topNTags.pop()
        topNTags.append([oldTag,totalWeight])
    topNTags.sort(key=itemgetter(1), reverse=True)

N = 10							# Change This to get Top N List
oldTag = None
totalWeight = 0
topNTags = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:					# Something has gone wrong. Skip this line.
        continue

    thisTag, thisWeight = data

    if oldTag and oldTag != thisTag:
        adder(oldTag, totalWeight)
        totalWeight = 0

    oldTag = thisTag
    totalWeight += int(thisWeight)			# Adds Particular Weight of Tag

adder(oldTag, totalWeight)
for i in range(len(topNTags)):
    print topNTags[i][0],"\t",topNTags[i][1]

