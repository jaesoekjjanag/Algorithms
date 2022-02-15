from sys import maxsize

def solution(nums):
  min_price = maxsize
  max_profit = 0
  
  for price in nums:
    min_price = min(price, min_price)
    max_profit = max(price-min_price, max_profit)
    
  return max_profit

print(solution([7,1,5,3,6,5]))