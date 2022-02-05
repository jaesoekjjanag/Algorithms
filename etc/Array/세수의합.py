# 합을 0으로 만들 수 있는 3개의 엘리먼트 조합

from collections import defaultdict

def solution(nums):
  nums.sort()
  results = []
  checked = []
  
  for i in range(len(nums)):
    target = -nums[i]
    if target in checked:
      continue
    
    checked.append(target)
    
    left = i+1
    right = len(nums)-1
    
    while(left < right):
      s = nums[left] + nums[right]
      if s == target:
        results.append([nums[i], nums[left], nums[right]])
        
        while left < right and nums[left] == nums[left+1]:
          left += 1
        while left < right and nums[right] == nums[right-1]:
          right -= 1
        
        left += 1
        right -=1 
        
      elif s > target:
        right -= 1
      else:
        left += 1
  
  return results
  
print(solution([-1,0,1,2,-1,-4]))

# 중복을 생략하지 않고 set으로 제거하는 풀이. 더 느리다.

def solution2(nums):
  nums.sort()
  ans=set()
  for i in range(len(nums)):
      target=-nums[i]
      start=i+1
      end=len(nums)-1
      while(start<end):
          summ=nums[start]+nums[end]
          if summ<target:
              start+=1
          elif summ>target:
              end-=1
          else:
              ans.add((nums[i],nums[start],nums[end]))
              start+=1
              end-=1
  return ans

print(solution2([-1,0,1,2,-1,-4]))