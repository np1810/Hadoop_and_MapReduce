#!/usr/bin/python
import sys

def printAllMaxIndices():
    k = max(hours)
    for i, j in enumerate(hours):		# Loop to get all the POSITIONS of the MAXIMUM in the hours
        if j == k:
            print oldAuthorId, "\t", i		# Print the hour with the maximum activity

oldAuthorId = None
hours = [0]*24					# List to hold the activity of the author_id

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:				# Something has gone wrong. Skip this line.
        continue

    thisId, thisHour = data

    if oldAuthorId and oldAuthorId != thisId:
        printAllMaxIndices()
        hours = [0]*24				# Re-initialize the list

    oldAuthorId = thisId
    hours[int(thisHour)] += 1			# Increase the frequency of the input hour

if oldAuthorId != None:
    printAllMaxIndices()

