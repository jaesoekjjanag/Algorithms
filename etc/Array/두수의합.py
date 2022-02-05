# 투포인터
#! nums는 항상 정렬되어있지 않기 때문에 이렇게 풀 수 없다. 정렬 하는 순간 원래 index가 마구 섞이기 때문.
def solution(nums, target):
  pl = 0
  pr = len(nums)-1
  
  while(pl < pr):
    sum = nums[pl] + nums[pr]
    if sum == target:
      return [pl, pr]
    elif sum > target:
      pr -=1
    elif sum < target:
      pl += 1
  
  
# print(solution([2,7,9,11], 9))


# 해시 테이블
def solution2(nums, target):
  hash_nums = {}
  for i, num in enumerate(nums):
    if (target - num) in hash_nums:
      return [hash_nums[target-num], i]
    hash_nums[num] = i
  
print(solution2([2,7,9,11], 9))
