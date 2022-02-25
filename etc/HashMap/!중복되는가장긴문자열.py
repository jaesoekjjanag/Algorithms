import collections

length = int(input())
s = input()

s_index = collections.defaultdict(list)
max_length = 0

for index, char in enumerate(s):
  indices = s_index[char]
  if indices:
    for i in indices:
      ptr1 = i
      ptr2 = index
      count = 0
      while True:
        if ptr1 < len(s) and ptr2 < len(s) and s[ptr1] == s[ptr2]:
          count += 1
          ptr1 += 1
          ptr2 += 1
        else: 
          break
      
      max_length = max(max_length, count)
      
  s_index[char].append(index)
  
print(max_length)
    
