#!/usr/bin/python
import sys

oldId = None
quesLength = 0
ansSum = 0.0
ansCount = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 3:			# Something has gone wrong. Skip this line.
        continue

    thisId, thisType, thisLen = data

    if oldId and oldId != thisId:
        if ansCount == 0:		# If the Question has NO Answer
            print "{0}\t{1}\t{2}".format(oldId, quesLength, 0)
        else:
            print "{0}\t{1}\t{2}".format(oldId, quesLength, ansSum/ansCount)
        quesLength = 0
        ansSum = 0.0
        ansCount = 0

    oldId = thisId
    if thisType == "A":			# If the Line is Question
        quesLength = int(thisLen)	# Save the Question Length
    elif thisType == "B":		# If the Line is Answer
        ansSum += float(thisLen)	# Find Total Length of all Answers
        ansCount += 1			# Find Number of Answers

if oldId != None:
    if ansCount == 0:
        print "{0}\t{1}\t{2}".format(oldId, quesLength, 0)
    else:
        print "{0}\t{1}\t{2}".format(oldId, quesLength, ansSum/ansCount)

