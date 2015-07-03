#!/usr/bin/python
import sys

oldId = None
studyGroup = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:			        # Something has gone wrong. Skip this line.
        continue

    thisId, thisAuthorId = data

    if oldId and oldId != thisId:
        print "{0}\t{1}".format(oldId, studyGroup)
        studyGroup = []

    oldId = thisId
    studyGroup.append(int(thisAuthorId))     # Making study groups

if oldId != None:
    print "{0}\t{1}".format(oldId, studyGroup)

