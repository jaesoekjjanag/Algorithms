from collections import deque

input = open('./input.txt').readline

n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]

direction = [
  [0, 1],
  [-1, 0],
  [0, -1],
  [1, 0]
]

def bfs(y, x, minY, minX, maxY, maxX, visited):
  q = deque([[y, x]])
  res = 0
  
  while q:
    y, x = q.popleft()
    visited[y][x] = 1
    res += people[y][x]

    for dy, dx in direction:    
      ny, nx = y+dy, x+dx
      if(minY<=ny<=maxY and minX<=nx<=maxX and not visited[ny][nx]):
        q.append([ny, nx])
      
  return res

def calc(y, x, d1, d2):
  population = [0]*(n+1)
  visited = [[0]*(n+1) for _ in range(n+1)]
  
  for i in range(1, d1):
    visited[y + i][x - i] = 1
    visited[y+i+d2][x-i+d2] = 1
  
  for i in range(1, d2):
    visited[y + i][x - i] = 1
    visited[y+i+d1][x-i+d1] = 1
    
  population[1] = bfs(0, 0, 0, 0, y+d1-1, x, visited)
  population[2] = bfs(0, n-1, 0, x+1, y+d2, n-1, visited)
  population[3] = bfs(n-1, 0, y+d1, 0, n-1, x-d1+d2, visited)
  population[4] = bfs(n-1, n-1, y+d2+1, x-d1+d2+1, n-1, n-1, visited)
  
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        population[5] += people[i][j]
        
  return max(population) - min(population)

answer = float('inf')

for y in range(n):
  for x in range(n):
    for d1 in range(n):
      for d2 in range(n):
        if(0<=y<y+d1+d2<n and 0<=x-d1<x<x+d2<n):
          answer = min(answer, calc(y, x, d1, d2))
          print(answer)
print(answer)