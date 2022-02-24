from collections import defaultdict

def solution(s):
  count = 0
  substring = defaultdict(int)
  
  for char in s:
    if substring[char] == 1:
      print(substring)
      substring.clear()
      
    substring[char] += 1
    count = max(len(substring), count)
    
  return count
  


print(solution("dvdf"))
