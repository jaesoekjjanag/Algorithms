from bisect import bisect_left

numbers = [0,0,2,3]
target = 0

def sum_index(numbers, target):
    for i in range(len(numbers)):
      expect = target-numbers[i]
      index = bisect_left(numbers, expect, i+1)
      if  index < len(numbers) and numbers[index] == expect: # 항상 배열 길이보다 작고, 원하는 값이 맞는지 체크해야 함.
        return [i+1, index+1]
    
print(sum_index(numbers, target))