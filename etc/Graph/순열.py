# 서로 다른 정수로 가능한 모든 수열

import itertools

def solution(nums):
  results = []
  perm = []
  
  def dfs(nums_left):
    if len(nums_left) == 0:
      print(perm)
      results.append(perm[:])
    
    for i in nums_left:
      perm.append(i)
      next_nums_left = nums_left[:]
      next_nums_left.remove(i)
      dfs(next_nums_left)
      perm.pop()
  
  dfs(nums)
  return results
print(solution([1,2,3]))

#순열 라이브러리
def solution2(nums):
  return list(itertools.permutations(nums))

print(solution2([1,2,3]))