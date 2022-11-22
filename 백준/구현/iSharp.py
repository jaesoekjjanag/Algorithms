import sys
import re

f = open('input.txt')

type, vars = f.readline().split(' ', 1)
vars = vars.split(', ')
op = ['*', '&', '[]']

for i, var in enumerate(vars):
  newType = type
  newVar = re.sub('\*|\&|\[]', '', var)
  replaced = re.findall('\*|\&|\[\]', var)
  
  newType += ''.join(replaced[::-1])
  
  if i != len(vars)-1:
    print("%s %s%s" %(newType, newVar, ";"))
  else:
    print("%s %s" %(newType, newVar))



