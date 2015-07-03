#!/usr/bin/python
import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)										# Ignoring FIELD name
for line in reader:
    if len(line) == 19:									# Ensuring the data is properly formatted
        hr = datetime.strptime(line[8].split('+')[0], "%Y-%m-%d %H:%M:%S.%f").hour	# Removing time offset using split and getting hour
        print line[3], "\t", hr								# Printing author_id and hour

