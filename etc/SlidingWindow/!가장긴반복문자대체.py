# s의 문자를 k번만큼 변경해서 만들 수 있는, 연속 문자열의 가장 긴 길이

from typing import Counter


s = "AABAABBB"
k = 2

counter = Counter()
left = right = 0

max_len = 0
for right in range(len(s)):
  counter[s[right]] += 1
  freq = counter.most_common(1)[0][1]
  
  if right-left+1-freq > k:
    left += 1
  max_len = max(right-left+1, max_len)
  
print(max_len)