import sys, os

f = open('./Divide_Conquer/쿼드트리_test.txt', 'r')

N = int(f.readline())
arr =[]

for _ in range(N):
  arr.append(list(f.readline().rstrip()))

def recursive(x, y, N):
  result =[]
  color = arr[x][y]

  for i in range(x, x+N):
    for j in range(y, y+N):
      if arr[i][j] != color and N//2 >0:
        result.append(recursive(x, y, N//2))
        result.append(recursive(x, y+N//2, N//2))
        result.append(recursive(x+N//2, y, N//2))
        result.append(recursive(x+N//2, y+N//2, N//2))
        return '('+''.join(result)+')'
      
  if color == '0':
    return '0'
  if color == '1':
    return '1'
  
result = recursive(0,0, N)
print(result)
