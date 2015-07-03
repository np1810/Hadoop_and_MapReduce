#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
for line in reader:
    txt=re.split(r'\s|[.,!?:;"()<>[\]#$=\-/]+',line[4])
    for seg in txt:
        if seg != "":
            print("{0}\t{1}").format(seg.lower(),line[0])

