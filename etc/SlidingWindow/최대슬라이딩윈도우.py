nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# r= []
# for i in range(len(nums)-k+1):
#   r.append(max(nums[i:i+k]))
  
# print(r)

# 큐를 이용한 최적화. 새로운 값이 이전 최대 값보다 큰 경우만 최대 값 갱신
from collections import deque


results = []
window = deque()
m = float('-inf')

for i, v in enumerate(nums):
  window.append(v)
  if i < k-1:
    continue
  
  if m == float('-inf'):
    m = max(window)
  
  if v > m:
    m = v
  
  results.append(m)
  
  if m == window.popleft():
    m = max(window)

print(results)