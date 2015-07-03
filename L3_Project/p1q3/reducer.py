#!/usr/bin/python

import sys

totalSales = 0
totalSalesValue = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 1:
        # Something has gone wrong. Skip this line.
        continue

    totalSalesValue += float(data_mapped[0])
    totalSales += 1

print totalSales, "\t", totalSalesValue

