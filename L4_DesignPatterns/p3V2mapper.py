#!/usr/bin/python
import sys
import csv
import re
from HTMLParser import HTMLParser

"""
Common words source (p3V2words.txt)
Only Top 100 words
wget --no-check-certificate https://github.com/first20hours/google-10000-english/raw/master/20k.txt && head -100 20k.txt > p3words.txt && rm -rf 20k.txt
Remove HTML Tags source
http://stackoverflow.com/a/925630

Don't Forget to give the file in Hadoop Command
hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper p3V2mapper.py -reducer p3V2reducer.py -file p3V2mapper.py -file p3V2reducer.py -input node -output p3V2output -file p3V2words.txt
"""

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def stripHTMLTags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

reader = csv.reader(sys.stdin, delimiter='\t')
next(reader)
p3words = open("p3V2words.txt").read()                          # Read Complete Common Words File
for num in range(0,10):                                         # Add numbers 0 to 9
    p3words += str(num)+"\n"
for line in reader:
    body = line[4].lower()
    try:
        body = stripHTMLTags(body)                              # Remove HTML Tags        
        wordList = re.split(r'\s|[.,!?:;"()<>[\]#$=\-/]+',body) # Split as instructed in problem
        for word in wordList:
            word = word.strip()
            if not word in p3words and re.match(r"^(?![0-9]*$)[\w]+$",word): # Word is NOT a Common Word but a Alphanumeric Word and not Purely Numeric
                print("{0}\t{1}").format(word,line[0])
    except UnicodeDecodeError as e:
        continue

