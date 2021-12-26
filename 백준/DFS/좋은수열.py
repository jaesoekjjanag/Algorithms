def validate(arr):
  length = len(arr)
  for i in range(length//2+1):
    for j in range(length//2):
      if(arr[i:i+j+1] == arr[i+j+1:2+2*j+i]):
        return False

  return True

def recursive(arr):
  endPoint = n
  while(len(arr) < endPoint):
    for i in numbers:
      arr.append(i)
      if(validate(arr)): #만약 새로 추가한 것이 좋은수열이라면
        recursive(arr)
        break
      else:
        arr.pop()
    
arr = []
numbers = ['1','2','3']

n = int(input())

if(n == 1):
  print(1)
else:
  recursive(arr)
  print(''.join(arr))