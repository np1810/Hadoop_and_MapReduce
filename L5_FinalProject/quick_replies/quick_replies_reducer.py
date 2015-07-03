#!/usr/bin/python
import sys
from datetime import datetime

oldId = None
sumOfDiff = 0.0                                             # Find the sum of differences of date
dateCount = 0                                               # Total different dates count
prevDate = None                                             # Storing previous date

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:                                      # Something has gone wrong. Skip this line.
        continue

    thisId, thisD = data
    thisDate = datetime.strptime(thisD, "%Y%m%d%H%M%S")     # Getting the date from data

    if oldId and oldId != thisId:
        ans = sumOfDiff/dateCount
        if ans != 0.0:
            print "{0:10.2f}\t{1:10d}".format(ans, int(oldId))
        dateCount = 0
        prevDate = None

    oldId = thisId
    if prevDate:
        sumOfDiff += float(abs((thisDate - prevDate).seconds))
    else:
        sumOfDiff = 0.0                                     # Will print 0.0 if only ONE date record exists
    dateCount += 1                                          # Else it'll print Average Activity Delay in Minutes
    prevDate = thisDate

if oldId != None:
    ans = sumOfDiff/dateCount
    if ans != 0.0:
        print "{0:10.2f}\t{1:10d}".format(ans, int(oldId))

