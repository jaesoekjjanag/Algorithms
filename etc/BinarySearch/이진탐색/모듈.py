from bisect import bisect_left

nums = [1,3,5,7,9,11]
target = 100

def search(nums, target):
  index = bisect_left(nums, target)
  
  try:
    if(nums[index] == target):
      return index
  except:
    return -1
  


print(search(nums, target))