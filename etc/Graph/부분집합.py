# 모든 부분집합 찾기

def solution(nums):
  results = [[]]
  
  def dfs(sub, nums):
    if sub:
      results.append(sub)      
      
    if not nums:
      return 
    
    for i in range(len(nums)):
      dfs(sub+[nums[i]], nums[i+1:])
      
  
  dfs([], nums)
  return results

print(solution([1,2,3]))