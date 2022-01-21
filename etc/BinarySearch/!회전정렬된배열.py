nums = [4,5,6,7,0,1,2,3]
target = 1

# (left + right)//2는 항상 right보다 크기 때문에 오버플로의 위험이 있다.
# left+(right - left)//2로 계산하면 right를 넘어서지 않고 같은 결과를 얻을 수 있다.

def search(nums, target):
  if not nums:
    return -1
  
  # 최솟값 찾기
  left, right = 0, len(nums)-1
  while(left <right):
    mid = left + (right - left)//2
    if(nums[mid] > nums[right]):
      left = mid +1
    else:
      right = mid
      
  pivot = left
  
  left, right = 0, len(nums)-1
  while(left <= right):
    mid = left + (right - left)//2
    mid_pivot = (mid + pivot) % len(nums) # 원래라면 가운데에 해당했을 좌표
    
    if(nums[mid_pivot] < target):
      left = mid + 1
    elif(nums[mid_pivot] > target):
      right = mid -1
    else:
      return mid_pivot
    
  return -1
    

print(search(nums, target))