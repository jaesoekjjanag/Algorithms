def solution(nums):
  nums.sort()
  result = 0
  
  for i in range(len(nums)):
    if i%2 == 0:
      result += nums[i]
      
  return result
  
print(solution([6,2,6,5,1,2]))
