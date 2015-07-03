#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)						# Ignoring FIELD name
for line in reader:
    if len(line) == 19 and line[5] == "question":	# Ensuring the data is properly formatted and Use only Question Tags
        for i in line[2].split():
            i = i.strip().lower()			# Trim Spaces and change to Lowercase for matching with Weights-List
            print "{0}\t{1}".format(i, "1")

