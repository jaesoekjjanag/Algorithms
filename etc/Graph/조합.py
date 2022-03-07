def solution(n, k):
  nums = list(range(1, n+1))
  results = []
  comb = []
  
  def dfs(nums_left):
    if len(comb) == k:
      return results.append(comb[:])
      
    if len(nums_left) == 0:
      return
      
    for i in range(len(nums_left)):
      comb.append(nums_left[i])
      next_nums_left = nums_left[i+1:]
      dfs(next_nums_left)
      comb.pop()
  
  dfs(nums)
  return results

print(solution(4, 2))