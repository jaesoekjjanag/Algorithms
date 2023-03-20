import sys
from collections import deque
# input = sys.stdin.readline
input = open('./벽 부수고 이동하기.txt').readline

n,m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
# visited = [[0]*m for _ in range(n)]
# visited[y][x][0]: 중간에 벽을 안부순 경우, visited[y][x][1]: 중간에 벽을 부순 경우
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] 
direction = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
]

answer = n*m
def bfs(y, x):
  queue = deque()
  queue.append((y, x, 0))
  
  while queue:
    y, x, crushed = queue.popleft()
    if y == n-1 and x == m-1:
      return visited[y][x][crushed]
    
    for dy, dx in direction:
      ny, nx = y+dy, x+dx
      
      if 0<=ny<n and 0<=nx<m:
        # 다음이 벽이고 아직 벽을 부수지 않은 경우
        if grid[ny][nx] == '1' and crushed == 0:
          # 벽 부수기
          visited[ny][nx][1] = visited[y][x][0] + 1
          queue.append((ny, nx, 1))
        
        elif grid[ny][nx] == '0' and visited[ny][nx][crushed] == 0:
          visited[ny][nx][crushed] = visited[y][x][crushed] + 1
          queue.append((ny, nx, crushed))
      
    return -1
print(bfs(0, 0))
# dfs 백트래킹. 시간초과
# def dfs(y, x, dist, crushed):
#   global answer
  
#   if(dist > answer):
#     return
  
#   if(y == n-1 and x == m-1):
#     answer = min(answer, dist)
  
#   if(grid[y][x] == '1'): 
#     if(crushed):
#       return
    
#     #벽이고 아직 한번도 부순적이 없는 경우
#     for dy, dx in direction:
#       ny, nx = y+dy, x+dx
#       if(0<=ny<n and 0<=nx< m and not visited[ny][nx]):
#         visited[ny][nx] = 1
#         dfs(ny, nx, dist+1, 1)
#         visited[ny][nx] = 0

#   else: 
#     for dy, dx in direction:
#         ny, nx = y+dy, x+dx
#         if(0<=ny<n and 0<=nx< m and not visited[ny][nx]):
#           visited[ny][nx] = 1
#           dfs(ny, nx, dist+1, crushed)
#           visited[ny][nx] = 0
      
# dfs(0, 0, 1, 0)
# print(answer if answer != n*m else -1)