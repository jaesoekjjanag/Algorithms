import sys
# input = sys.stdin.readline
input = open('./로봇청소기.txt').readline

n, m = map(int, input().split())
y, x, d = map(int, input().split()) # d 북:0 동:1 남:2 서:3
room = [list(map(int, input().split())) for _ in range(n)] # 0: 청소되지 않음, 1: 벽, 2: 청소됨

direction = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1]
]
head = direction[d]

def lookAround(y, x):
  result = False
  
  for dy, dx in direction:
    ny, nx = y+dy, x+dx
    if(0<=ny<n and 0<=nx<m and room[ny][nx] == 0):
      result = True
      
  return result    

answer = 0
while 1:
  if(room[y][x] == 0):
    room[y][x] = 2
    answer += 1
    
  if(lookAround(y, x)): #빈 칸이 있는 경우 방향전환
    d = (d+3)%4
    dy, dx = direction[d]
    ny, nx = y+dy, x+dx
    if(0<=ny<n and 0<=nx<m and room[ny][nx] == 0):
      y, x = ny, nx
      
  else: #청소되지 않은 빈 칸이 없는 경우
    dy, dx = direction[(d+2)%4]
    ny, nx = y+dy, x+dx
    if(0<=ny<n and 0<=nx<m and room[ny][nx] == 2): #후진
      y, x = ny, nx
    else:
      break

print(answer)