# 서로 다른 정수로 가능한 모든 수열

def solution(nums):
  def dfs(index, available, path):
    if index == len(nums):
      return results.append(path)
    
    for i in available:
      nextAvailable = available[:]
      nextAvailable.remove(i)
      dfs(index+1, nextAvailable, path+[i])
  
  results = []
  dfs(0, nums, [])
    
  return results

print(solution([1,2,3]))

# #순열 라이브러리
# import itertools

# def solution2(nums):
#   return list(itertools.permutations(nums))

# print(solution2([1,2,3]))

