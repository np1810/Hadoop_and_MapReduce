#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
oldKey = None
karma = []
out = []
for line in reader:
    if len(line) == 6 or len(line) == 10:
        if line[1] == "A":
            karma = []
            karma.extend((line[2],line[3],line[4],line[5]))

        elif line[1] == "B":
            out = []
            out.extend((line[2],line[3],line[4],line[0],line[5],line[6],line[7],line[8],line[9]))
            if len(karma) == 4:
                out.extend((karma[0],karma[1],karma[2],karma[3]))
            writer.writerow(out)

