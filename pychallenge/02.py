#!/usr/bin/env python3

import string
from urllib.request import urlopen

problem_url = "http://www.pythonchallenge.com/pc/def/ocr.html"

with urlopen(problem_url) as source_file:
  source = source_file.read().decode()

source = source.split("\n")
in_goo = False
secret = []

for line in source:
  if in_goo == False and "mess below" in line:
    in_goo = True
  elif in_goo == True:
    for char in line:
      if char in string.ascii_lowercase:
        secret.append(char)

secret = "".join(secret)

print("http://www.pythonchallenge.com/pc/def/" + secret + ".html")
