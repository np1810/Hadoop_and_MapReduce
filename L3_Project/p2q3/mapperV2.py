#!/usr/bin/python

# Format of each line is:
# 10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
# %h %l %u %t \"%r\" %>s %b

import sys
from urlparse import urlparse

for line in sys.stdin:
	line = line.strip()
	s = line.index("\"")
	e = line.rindex("\"")
	if(s != e):
		url = urlparse(line[s+1:e].split(" ")[1])
		print "{0}\t".format(url.path)

# This should have been the proper solution because url's parameters or arguments, etc should NOT
# be considered while finding the most accessed file.
# Example:-
# /displaytitle.php?uid=xyz		COUNT = 1
# /displaytitle.php?uid=abc		COUNT = 2

