from collections import defaultdict

def solution(s):
  used = {}
  length = start = 0
  
  for index, char in enumerate(s):
    if char in used and start <= used[char]: 
      start = used[char] + 1
    else:
      length = max(length, index - start + 1)
      
    used[char] = index 
    
  return length

print(solution("abcabcbb"))
print(solution("tmmzuxt"))
print(solution('dbdf'))
print(solution('bbbbb'))
