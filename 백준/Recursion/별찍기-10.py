N = int(input())
grid = [[' ']*N for _ in range(N)]

def recursion(n, x, y):
  if n == 1:
    return
  
  
  d = int(n/3)
  for i in range(3):
    for j in range(3):
      if not(i==1 and j==1):
        recursion(d, x+i*d, y+j*d)
        if d==1:
          global grid
          grid[x+i][y+j] = '*'
  
recursion(N, 0, 0)

for i in range(N):
  for j in range(N):
    print(grid[i][j], end='')
  print()

