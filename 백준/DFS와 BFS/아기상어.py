from collections import deque

f = open("./아기상어.txt")

n = int(f.readline().rstrip())
grid = [list(map(int, f.readline().rstrip().split())) for i in range(n)] 

def bfs(grid, shark, node):
  Q = deque([node])
  d = [[-1, 0], [0, -1], [0, 1], [1, 0]]
  n = len(grid)
  visited = [[0] * n for i in range(n)]
  fishes =[] 
  
  while(Q):
    [i, j] = Q.popleft()
    
    time = visited[i][j]
    fish = grid[i][j]
    
    if(fish and fish < shark):
      fishes.append([i, j, time])
      # return [[i, j], time]    
    
    for di, dj in d:
      nextI =  i + di
      nextJ = j + dj
      if(nextI < n and nextJ < n and nextI >=0 and nextJ >=0 and not visited[nextI][nextJ]):
        if(grid[nextI][nextJ] <= shark):
          visited[nextI][nextJ] = time + 1
          Q.append([nextI, nextJ])
          
  if fishes:
    fishes.sort(key = lambda x: (x[2], x[0], x[1] ))
    fish = fishes[0]
    grid[fish[0]][fish[1]] = 0
    return [[fish[0], fish[1]], fish[2]]
  return [shark, 0]
        
  
shark = 2
exp = 2
time = 0
node = [0, 0]
for i in range(n):
  for j in range(n):
    if grid[i][j] == 9:
      node = [i, j]
      grid[i][j] = 0

while(True):
  [n, t] = bfs(grid, shark, node)
  if not t:
    break
  exp -= 1
  if exp == 0:
    shark += 1
    exp = shark
  node = n
  time += t

print(time)

  