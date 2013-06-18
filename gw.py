#!/usr/bin/python

import feedparser
import re

d =  feedparser.parse('http://w1.weather.gov/xml/current_obs/KBOS.rss')
x = format(d.entries[0].summary)
s = re.split("[\n]",x)
print d.entries[0].title
print s[1]
