#!/usr/bin/env python3

import re
from urllib.request import urlopen

nothing_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothings    = ["12345"]

while True:
  with urlopen(nothing_url + nothings[-1]) as nothing_file:
    nothing_source = nothing_file.read().decode()
  print(nothing_source)
  if "Divide by two" in nothing_source:
    nothings.append((str(int(nothings[-1])/2)))
  else:
    numbers = re.findall("[0-9]+",nothing_source)
    if numbers: # we need the last number, to skip the trap
      nothings.append(numbers[-1])
    else: # in the end, there is just the secret url part
      print("http://www.pythonchallenge.com/pc/def/" + nothing_source.strip())
      break
