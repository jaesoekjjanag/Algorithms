# j는 보석, s는 갖고 있는 돌. 몇 개의 보석을 가지고 있는가

from collections import defaultdict


def solution(j, s):
  result = 0
  
  freq = defaultdict(int)
  
  for char in s:
    freq[char] += 1
    
  for gem in j:
    result += freq[gem] #defaultdict이기 때문에 존재 여부를 확인하지 않아도 됨
      
  return result

print(solution("aA", "aAAbbbb"))

# from collections import Counter

# def solution(j, s):
#   result = 0;
  
#   freq = Counter(s)
  
#   for gem in j:
#     result += freq[gem]
  
#   return result

# print(solution("aA", "aAAbbbb"))
