import sys, os

f = open('./Divide_Conquer/색종이만들기_test.txt', 'r')

N = int(f.readline())
arr = [list(map(int, f.readline().rstrip().split())) for _ in range(N)] 

blue = [];
white = [];

def recursive(x, y, N):
  color = arr[x][y]
  for i in range(x, x+N):
    for j in range(y, y+N):
      if arr[i][j] != color:
        recursive(x, y, N//2)
        recursive(x+N//2, y, N//2)
        recursive(x, y+N//2, N//2)
        recursive(x+N//2, y+N//2, N//2)
        return
    
  if color == 1:
    blue.append(color)
  else:
    white.append(color)
    
recursive(0,0, N)
print(len(white))
print(len(blue))
  