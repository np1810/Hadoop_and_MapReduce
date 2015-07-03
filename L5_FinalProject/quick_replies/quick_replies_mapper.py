#!/usr/bin/python
import sys
import csv
from datetime import datetime

# To get the Quickest Replies IDs, give command on output file as "sort -n quick_replies_output.tsv | head"

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)										                            # Ignoring FIELD name
for line in reader:
    if len(line) == 19:									                        # Ensuring the data is properly formatted
        nodeType = line[5]                                                      # Getting node_type for getting proper id
        if nodeType == "question":
            idNum = line[0]
        else:
            idNum = line[6]
        d = datetime.strptime(line[8].split('+')[0], "%Y-%m-%d %H:%M:%S.%f")	# Removing time offset using split
        print idNum, "\t", d.strftime("%Y%m%d%H%M%S")                           # Printing ques_id/parent_id, date time and post title

