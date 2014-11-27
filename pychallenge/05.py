#!/usr/bin/env python3

import pickle
from urllib.request import urlopen

pickle_url = "http://www.pythonchallenge.com/pc/def/banner.p"
with urlopen(pickle_url) as pickle_file:
  pickle_data = pickle.load(pickle_file)

for ppdd in pickle_data:
  for pd in ppdd:
    print(pd[0]*pd[1], end="")
  print()
