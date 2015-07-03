#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)                                            # Ignoring FIELD name
for line in reader:
    if len(line) == 19:                                 # Ensuring the data is properly formatted
        nodeType = line[5]                              # Get the node_type i.e. question, answer or comment
        if nodeType == "question":
            print "{0}\t{1}".format(line[0], line[3])   # Print ID and Author_ID
        else:
            print "{0}\t{1}".format(line[6], line[3])   # Print Parent_ID and Author_ID

