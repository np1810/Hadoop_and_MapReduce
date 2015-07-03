#!/usr/bin/python
import sys
import csv

# Don't Forget to give the file in Hadoop Command
# hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper popular_tags_extra_mapper.py -reducer popular_tags_extra_reducer.py -file popular_tags_extra_mapper.py -file popular_tags_extra_reducer.py -input node -output popular_tags_extra -file popular_tags_extra_weights.tsv

def getWeight(s):
    r = csv.reader(open('popular_tags_extra_weights.tsv'), delimiter='\t')
    for l in r:
        if len(l)==2 and l[1] == s:
            return int(l[0])
    return 1

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)                                        # Ignoring FIELD name
for line in reader:
    if len(line) == 19 and line[5] == "question":	# Ensuring the data is properly formatted and Use only Question Tags
        for i in line[2].split():
            i = i.strip().lower()                   # Trim Spaces and change to Lowercase for matching with Weights-List
            print "{0}\t{1}".format(i, getWeight(i))

