import sys

n = int(sys.stdin.readline().rstrip())

visited = []
count = 0

def attackable(r, c):
  for i, j in visited:
    if i == r or j == c or (r+c) == (i+j) or (r-c) == (i-j):
      return True
  return False

def dfs(r, c):
  global count
  if r == n-1:
    count += 1
    return 

  visited.append([r, c])
  
  for i in range(n):
    if attackable(r+1, i):
      continue
    
    dfs(r+1, i)

  visited.pop()

for i in range(n//2):
  dfs(0, i)
  
count *= 2

if(n%2):
  dfs(0, n//2)
    
print(count)
  


