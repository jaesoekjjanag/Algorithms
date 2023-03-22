input = open('./input.txt').readline
n, m, t = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

top = 0
bot = 0

for i in range(n):
  if grid[i][0] == -1:
    if not top:
      top = i
    else:
      bot = i
      
def diffuse():
  direction = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1]
  ]

  temp = [[0]*m for _ in range(n)]
  
  for y in range(n):
    for x in range(m):
      if(grid[y][x] > 0):
        amount = grid[y][x]
        count = 0
        
        for dy, dx in direction:
          ny, nx = y+dy, x+dx
          if(0<=ny<n and 0<=nx<m and grid[ny][nx]!=-1):
            temp[ny][nx] += amount//5
            count += 1
            
        grid[y][x] -= count*(amount//5)
        
  for y in range(n):
    for x in range(m):
      grid[y][x] += temp[y][x]

def circulate(circulator, direction):
  d = 0
  last = 0
  y, x = circulator, 1
  while 1:
    ny, nx = y+direction[d][0], x+direction[d][1]
    
    if(y == circulator and x == 0):
      break
    
    if(ny < 0 or ny >= n or nx < 0 or nx >= m):
      d+=1
      continue
      
    grid[y][x], last = last, grid[y][x]
    y, x = ny, nx

for _ in range(t):
  diffuse()
  circulate(top, [
    [0, 1],
    [-1, 0],
    [0, -1],
    [1, 0]
  ])
  circulate(bot, [
    [0, 1],
    [1, 0],
    [0, -1],
    [-1, 0]
  ])

answer = 0
for i in range(n):
  for j in range(m):
    if grid[i][j] > 0:
      answer += grid[i][j]

print(answer)