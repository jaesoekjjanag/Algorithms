from typing import Counter

name = list(input())
name.sort()

length = len(name)

l1 = []
l2 = []
l3 = []

counter = Counter(name)

for key, value in counter.items():
  for _ in range(value // 2):
    l1.append(key)
    l2.append(key)
  
  if(value%2):
    for _ in range(value%2):
      l3.append(key)

if len(l3) > 1 or (not length%2 and l3):
  print("I'm Sorry Hansoo")
else:
  print(''.join(l1+l3+l2[::-1]))


