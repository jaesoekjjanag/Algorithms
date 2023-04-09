# 활성 상태는 4방향으로 1초 후 복제, 비활성 바이러스를 활성 바이러스로 바꾼다
# M개의 바이러스를 활성상태로 만들기

import sys
from itertools import combinations
from collections import deque

input = open('./input.txt').readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]

candidates = []
blank_count = 0

for i in range(n):
  for j in range(n):
    if(lab[i][j] == 2):
      candidates.append((i, j))
    if(lab[i][j] == 0):
      blank_count += 1
      
candidate_count = len(candidates)
if(candidate_count == 0):
  print(0)
  sys.exit(0)

candidates = list(combinations(candidates, 3))
direction = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1]
]

def check(arr):
  return sum(map(lambda x: 0 in x, arr))

def bfs(active):
  Q = deque(active)
  virus = [[-1] * n for _ in range(n)]
  res = 0
  
  for y, x in active:
    Q.append((y, x))
    virus[y][x] = 0
  
  while Q:
    y, x = Q.popleft()
    time = virus[y][x]
    
    for dy, dx in direction:
      ny, nx = y+dy, x+dx
      if(0<=ny<n and 0<=nx<n and virus[nx][ny] == -1):
        if(lab[ny][nx] == 0):
          Q.append((ny, nx))
          virus[ny][nx] = time + 1
          res = max(time, res)
  
  for i in range(n):
    for j in range(n):
      if lab[i][j] == 0 and virus[i][j] == -1:
        return -1

  return res

time = 0
for active in candidates:
  print(bfs(active))
    
    
