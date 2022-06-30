# Timeout

n = int(input())

grid = [[0]*n for _ in range(n)]

def attackable(r, c):
  for i in range(r):
    for j in range(n):
      if grid[i][j] == 1:
        if i == r or j == c or (r+c) == (i+j) or (r-c) == (i-j):
          return True
      
  return False

count = 0

def dfs(r, c):
  global count
  if attackable(r, c):
    return 

  if r == n-1:
    count += 1
    return

  grid[r][c] = 1
  
  for i in range(n):
    dfs(r+1, i)
    grid[r+1][i] = 0

for i in range(n):
  dfs(0, i)
  grid[0][i] = 0

print(count)

