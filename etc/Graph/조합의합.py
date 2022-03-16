# 조합하여 target을 만들 수 있는 candidates. 중복 가능

def solution(candidates, target):
  def dfs(index, target, path):
    if target < 0:
      return
    
    if target == 0:
      return results.append(path)
    
    for i in range(index, len(candidates)):
      dfs(i, target-candidates[i], path+[candidates[i]])
    
    return
  
  results = []  
  dfs(0, target, [])
  
  return results

print(solution([2,3,6,7], 7));
print(solution([2,3,5], 8))