nums = [1,3,5,7,9,11]
target = 3

def binary_search(nums, target):
  left = 0
  right = len(nums)-1
  
  while(left <= right):
    mid = (left + right)//2
    if(nums[mid] == target):
      return mid
    elif(nums[mid] > target):
      right = target-1
    else:
      left = target+1
      
  return -1
  
print(binary_search(nums, target))