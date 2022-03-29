# NxN 정사각형을 (N/3)*(N/3)만큼 뚫기

n = int(input())
grid = [[False]*n for _ in range(n)]

def recursion(n, x, y):
  if n == 1:
    return
  
  global grid
  
  d = int(n/3)
  for i in range(3):
    for j in range(3):
      if not(i==1 and j==1):
        recursion(d, x+i*d, y+j*d)
        if d==1:
          grid[x+i][y+j] = True
  
recursion(n, 0, 0)

for i in range(n):
  for j in range(n):
    if grid[i][j]:
      print('*', end='')
    else:
      print(' ', end='')
  print()