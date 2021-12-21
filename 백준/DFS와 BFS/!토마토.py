# 익은 토마토는 1, 익지 않은 토마토는 0, 비어있으면 -1
# 익지 않은 토마토는 옆에 있는 익은 토마토에 의해 하루 뒤 익는다. 대각선에는 영향을 주지 못함
# 최소 며칠 뒤에 모든 토마토가 익는가?

from collections import deque

m, n = map(int, input().split())

box = [list(map(int, input().split())) for i in range(n)]

queue = deque();

for i in range(n):
  for j in range(m):
    if(box[i][j] == 1):
      queue.append([i, j])
      
move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
  while len(queue) > 0:
    [x, y] = queue.popleft()
    for dx, dy in move:
      if(x+dx >= 0 and x+dx <n and y+dy >=0 and y+dy <m):
        if(box[x+dx][y+dy] == 0):
          box[x+dx][y+dy] = box[x][y] + 1
          queue.append([x+dx, y+dy])

bfs()

max = 0 
for i in range(n):
  for j in range(m):
    day = box[i][j]
    if(day > max):
      max = day
    if(day == 0):
      print(-1)
      exit()

print(max-1)