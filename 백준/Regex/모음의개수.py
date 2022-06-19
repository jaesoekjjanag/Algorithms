f = open("모음의개수.txt")

import re

r = re.compile("[aeiou]", re.I)
while(True):
  line = f.readline().rstrip()
  if line == '#': break;
  
  print(len(r.findall(line)))
  
  