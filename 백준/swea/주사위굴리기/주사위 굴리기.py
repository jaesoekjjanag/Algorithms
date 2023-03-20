# 도착한 칸이 0이면 주사위 바닥의 값으로 변경
# 도착한 칸이 0이 아니면 주사위 바닥이 그 갑스로 변경, 지도의 값은 0으로

import sys
input = open('./주사위 굴리기.txt').readline

n, m , y, x, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] 
order = list(map(int, input().split()))
direction = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]
dice = [0]*7

TOP = 1
BOT = 6

def rollLeft():
  top = dice[1]
  dice[1] = dice[3]
  dice[3] = dice[6]
  dice[6] = dice[4]
  dice[4] = top

def rollRight():
  top = dice[1]
  dice[1] = dice[4]
  dice[4] = dice[6]
  dice[6] = dice[3]
  dice[3] = top

def rollTop():
  top = dice[1]
  dice[1] = dice[5]
  dice[5] = dice[6]
  dice[6] = dice[2]
  dice[2] = top

def rollBot():
  top = dice[1]
  dice[1] = dice[2]
  dice[2] = dice[6]
  dice[6] = dice[5]
  dice[5] = top

def roll(o):
  if(o == 1):
    rollRight()
  if(o == 2):
    rollLeft()
  if(o == 3):
    rollTop()
  if(o == 4):
    rollBot()

for o in order:
  dy, dx = direction[o]
  ny, nx = y+dy, x+dx
  if(0<=ny<n and 0<=nx<m):
    roll(o)
    y, x = ny, nx
    print(dice[TOP])
    if(grid[y][x] == 0):
      grid[y][x] = dice[BOT]
    else:
      dice[BOT] = grid[y][x]
      grid[y][x] = 0
      