from collections import deque

f = open('적록색약.txt')

n = int(f.readline().rstrip())

visited = [[0]*n  for _ in range(n)]
drawing = [list(f.readline().rstrip()) for _ in range(n) ]


# def bfs(drawing, i, j):
#   color = drawing[i][j]
  
#   Q = deque()
#   Q.append([i, j])
  
#   direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  
  
#   while(Q):
#     # x가 행인걸 잊지 않기
#     x, y = Q.popleft()
#     visited[x][y] = 1 
    
#     for [dx, dy] in direction:
#       nextX = x+dx
#       nextY = y+dy
      
#       if(nextX < n and nextY< n and nextX >=0 and nextY >=0 and visited[nextX][nextY] == 0  and  drawing[nextX][nextY] == color):
#         Q.append([nextX, y+dy])

direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  

def dfs(x, y):
  color = drawing[i][j]

  visited[x][y] = 1 
  
  for [dx, dy] in direction:
    nextX = x+dx
    nextY = y+dy
    
    if(nextX < n and nextY< n and nextX >=0 and nextY >=0 and visited[nextX][nextY] == 0  and  drawing[nextX][nextY] == color):
      dfs(nextX, nextY)

count_normal = 0

for i in range(n):
  for j in range(n):
    if(visited[i][j] == 1):
      continue
    
    count_normal += 1
    dfs(i, j)


visited = [[0]*n  for _ in range(n)]
count_blind = 0

for i in range(n):
  for j in range(n):
    if(drawing[i][j] == 'G'):
      drawing[i][j] = 'R'

for i in range(n):
  for j in range(n):
      
    if(visited[i][j] == 1):
      continue
    
    count_blind += 1
    dfs(i, j)

    
print(count_normal, count_blind)
      