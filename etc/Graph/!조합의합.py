# 조합하여 target을 만들 수 있는 candidates. 중복 가능

candidates = [2,3,6,7] 
target = 7

def solution(candidates, target):
  results = []
  
  def dfs(target, index, path):
    if target == 0:
        results.append(path)
        return
      
    if target < 0:
      return
    
    for i in range(index, len(candidates)):
      candidate = candidates[i]
      dfs(target - candidate, i, path + [candidate])
  
  dfs(target, 0, [])
  
  return results
  
print(solution(candidates, target))