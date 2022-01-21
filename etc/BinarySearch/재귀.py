nums = [1,3,5,7,9,11]
target = 3

def binary_search(left, right):
  if left <= right:
    mid = (left + right)//2
    
    if nums[mid] < target:
      return binary_search(mid+1, right)
    elif nums[mid] > target:
        return binary_search(left, mid-1)
    else:
      return mid
    
  else:
    return -1

print(binary_search(0, len(nums)-1))
