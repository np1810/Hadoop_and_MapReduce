#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b

import sys

for line in sys.stdin:
	line = line.strip()
	s = line.index("\"")
	e = line.rindex("\"")
	if(s != e):
		string = line[s+1:e].replace("http://www.the-associates.co.uk","",1)
		url = string.split(" ")[1]
		print "{0}\t".format(url)

# Final Answer can be found using the shell command given below
# cat outputp2q3.tsv | sort -n | tail

