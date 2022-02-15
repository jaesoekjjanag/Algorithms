#내 풀이
from functools import reduce

def solution(nums):
  mult = reduce(lambda x, y: x*y, nums)
  
  def elem(x):
    if x == 0:
      newNums = nums[:]
      newNums.remove(x)
      return reduce(lambda x, y: x*y, newNums)
    else:
      return int(mult/x)
  
  nums = list(map(lambda x: elem(x), nums))
  return nums

print(solution([1,2,3,4]))

#! 나눗셈을 사용하지 않아야 한다. => 내 풀이는 사용할 수 없다.
# 자기 자신을 제외하고 왼쪽 숫자들의 곱 * 오른쪽 숫자들의 곱.
def solution(nums):
  out = []
  p = 1
  for i in range(len(nums)):
    out.append(p)
    p = p * nums[i]
  
  p=1
  for i in range(len(nums)-1, -1, -1):
    out[i] = out[i] * p
    p = p * nums[i]
  
  return out