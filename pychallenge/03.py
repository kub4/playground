#!/usr/bin/env python3

import re
from urllib.request import urlopen

problem_url = "http://www.pythonchallenge.com/pc/def/equality.html"

with urlopen(problem_url) as source_file:
  source = source_file.read().decode()

source = source.split("\n")

for i, line in enumerate(source):
  if "<!--" in line:
    goo = "".join(source[i+1:])
    break

secret = "".join(re.findall("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", goo))

print("http://www.pythonchallenge.com/pc/def/" + secret + ".html")
