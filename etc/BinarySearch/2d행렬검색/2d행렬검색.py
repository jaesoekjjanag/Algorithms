arr = [
  [1,4,7,11,15],
  [2,5,8,12,19],
  [3,6,9,16,22],
  [10,13,14,17,24],
  [18,21,23,26,30]
]

target = 5

# def search(arr, target):
#   row = 0
#   col = len(arr[0])-1
  
#   while(row <=len(arr)-1 and col >=0):
#     crnt = arr[row][col]
#     if target == crnt:
#       return True
#     elif target > crnt:
#       row += 1
#     else:
#       col -= 1

def search(arr, target):
  return any([target in row for row in arr])
      
print(search(arr, target))
    