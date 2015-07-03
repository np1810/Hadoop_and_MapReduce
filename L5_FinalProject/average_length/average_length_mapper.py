#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)				# Ignoring FIELD name
for line in reader:
    if len(line) == 19:			# Ensuring the data is properly formatted
        nodeType = line[5]		# Print the ID/ParentID, A/B for Question/Answer and Length of Body
        if nodeType == "question":
            print "{0}\t{1}\t{2}".format(line[0], "A", len(line[4]))
        elif nodeType == "answer":
            print "{0}\t{1}\t{2}".format(line[6], "B", len(line[4]))

