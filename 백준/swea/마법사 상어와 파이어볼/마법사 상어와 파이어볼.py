from collections import deque

input = open('./input.txt').readline

n, m, k = map(int, input().split())
grid = [[[] for _ in range(n+1)] for _ in range(n+1)]

direction = {
  0: [-1, 0],
  1: [-1, 1],
  2: [0, 1],
  3: [1, 1],
  4: [1, 0],
  5: [1, -1],
  6: [0, -1],
  7: [-1, -1],
}

divided_directions = [[1,3,5,7], [0,2,4,6]]

fireballs = []
for _ in range(m):
  r, c, m, s, d = map(int, input().split()) #위치, 질량, 속력, 방향
  grid[r][c].append([m, s, d])
  # fireballs.append([r, c, m, s, d])
  fireballs.append([r, c])

def move():
  for y, x in fireballs:
    m, s, d = grid[y][x].pop()
    dy, dx = direction[d]
    ny, nx = y + s*dy, x + s*dx
    grid[ny][nx].append([m, s, d])

def divide():
  q = deque([])
  
  for y in range(n):
    for x in range(n):
      if(len(grid[y][x])>=2):
        q.append([y, x])
      
  while(q):
    y, x = q.popleft()
    acc_m, acc_s, count = 0, 0, len(grid[y][x])
    last_direction = grid[y][x][0][2]%2
    is_all_direction_same = 1
    
    while(grid[y][x]):
      m,s,d = grid[y][x].pop()
      acc_m += m
      acc_s += s
      if(d%2 != last_direction):
        is_all_direction_same = 0
    
    m = acc_m//5
    s = acc_s//count
    d = divided_directions[is_all_direction_same]
    
    if(m == 0): continue
        
    for nd in d:
      dy,dx = direction[nd]
      ny, nx = y+s*dy, x+s*dx
      grid[ny][nx].append([m, s, nd])
      if(len(grid[ny][nx])>=2):
        q.append([ny, nx])
  
def order():
  move()
  divide()
  
for _ in range(k):
  order()

answer = 0
print(grid)
for y in range(1, n+1): 
  for x in range(1, n+1):
    print(grid[y][x])
  
print(answer)