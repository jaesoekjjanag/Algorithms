# T의 모든 문자가 포함된 최소 윈도우

from typing import Counter


s = "ADOBECODEBANC"
t = "ABC"

need = Counter(t)
missing = len(t)

left = start = end = 0

for right, char in enumerate(s, 1):
  missing -= need[char] > 0
  need[char] -= 1
  
  if missing == 0:
    while left < right and need[s[left]] < 0:
      need[s[left]] += 1
      left += 1
      
    if not end or right - left <= end - start:
      start, end = left, right
      need[s[left]] += 1
      missing += 1
      left += 1
      
print(s[start:end])

# min_length = len(T)

# def search(c, ptrs, i):
#   temp = ptrs[i]
  
#   while temp < len(S)-1:
#     print(temp, S[temp], c)
#     if S[temp] == c:
#       ptrs[i] = temp
#       return False
    
#     temp += 1
  
#   return True

# min_length = len(S)
# ptrs = [0]*len(S)

# while(True):
#   noChange = True
#   for i in range(len(T)):
#     noChange = noChange and search(T[i], ptrs, i)
    
#   if noChange:
#     break
  
#   min_length = min(min_length, max(ptrs) - min(ptrs))

# print(min_length)

