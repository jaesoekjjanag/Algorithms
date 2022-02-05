# 비가 온 후 멀마나 많은 물이 쌓일 수 있는가

# 투포인터 풀이... 이걸 어떻게 생각해내지
def solution(heights):
  if not heights:
    return 0
  
  result = 0
  
  left, right = 0, len(heights)-1
  left_max, right_max = heights[left], heights[right]
  
  while(left < right):
    left_max = max(left_max, heights[left])
    right_max = max(right_max, heights[right])
    
    if left_max <= right_max:
      result += left_max - heights[left]
      left += 1
    else:
      result += right_max - heights[right]
      right -= 1

  return result

print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))

      