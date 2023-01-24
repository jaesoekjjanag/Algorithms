# 미친 풀이

import copy
f = open('./감시.txt')

ip = f.readline;

N, M = map(int, ip().split());
room = [list(map(int, ip().split())) for _ in range(N)] 

cctvs = []

for i in range(N):
  for j in range(M):
    x = room[i][j]
    if(x == 0 or x == 6): continue
    else: cctvs.append([i, j]) 

def up(i, j, room):
  for k in range(i-1, -1, -1):
    x = room[k][j]
    if x == 6:
      break
    if not x:
      room[k][j] = '#'

def down(i, j, room):
  for k in range(i+1, N):
    x = room[k][j]
    if x == 6:
      break
    if not x:
      room[k][j] = '#'
      
def left(i, j, room):
  for k in range(j-1, -1, -1):
    x = room[i][k]
    if x == 6:
      break
    if not x:
      room[i][k] = '#'
    
def right(i, j, room):
  for k in range(j+1, M):
    x = room[i][k]
    if x == 6:
      break
    if not x:
      room[i][k] = '#' 

answer = 64
def dfs(n, room):
  global answer
  if(n == len(cctvs)):
    answer = min(answer, sum(room[i].count(0) for i in range(N)))
    return 
  
  [i, j] = cctvs[n]
  x = room[i][j]
  if(x == 1):
    room1 = copy.deepcopy(room[::])
    left(i, j, room1)
    dfs(n+1, room1)
    
    room2 = copy.deepcopy(room[::])
    right(i, j, room2)
    dfs(n+1, room2)
    
    room3 = copy.deepcopy(room[::])
    up(i, j, room3)
    dfs(n+1, room3)
    
    room4 = copy.deepcopy(room[::])
    down(i, j, room4)
    dfs(n+1, room4)

  if(x == 2):
    room1 = copy.deepcopy(room[::])
    left(i, j, room1)
    right(i, j, room1)
    dfs(n+1, room1)
    
    room2 = copy.deepcopy(room[::])
    up(i, j, room2)
    down(i, j, room2)
    dfs(n+1, room2)
    
  if(x == 3):
    room1 = copy.deepcopy(room[::])
    right(i, j, room1)
    up(i, j, room1)
    dfs(n+1, room1)
    
    room2 = copy.deepcopy(room[::])
    left(i, j, room2)
    up(i, j, room2)
    dfs(n+1, room2)
    
    room3 = copy.deepcopy(room[::])
    left(i, j, room3)
    down(i, j, room3)
    dfs(n+1, room3)
    
    room4 = copy.deepcopy(room[::])
    right(i, j, room4)
    down(i, j, room4)
    dfs(n+1, room4)
    
  if(x == 4):
    room1 = copy.deepcopy(room[::])
    left(i, j, room1)
    right(i, j, room1)
    up(i, j, room1)
    dfs(n+1, room1)
    
    room2 = copy.deepcopy(room[::])
    left(i, j, room2)
    up(i, j, room2)
    down(i, j, room2)
    dfs(n+1, room2)
    
    room3 = copy.deepcopy(room[::])
    left(i, j, room3)
    right(i, j, room3)
    down(i, j, room3)
    dfs(n+1, room3)
    
    room4 = copy.deepcopy(room[::])
    right(i, j, room4)
    up(i, j, room4)
    down(i, j, room4)
    dfs(n+1, room4)
    
  if(x == 5):
    room1 = copy.deepcopy(room[::])
    left(i, j, room1)
    right(i, j, room1)
    up(i, j, room1)
    down(i, j, room1)
    dfs(n+1, room1)
    
dfs(0, room)

print(answer)