import sys
sys.setrecursionlimit(10**7)

f = open('두 동전.txt')

n, m = map(int, f.readline().rstrip().split())

board = [list(f.readline().rstrip())  for _ in range(n)]

y1 = -1
x1 = -1
y2 = -1
x2 = -1

for i in range(n):
  for j in range(m):
    if board[i][j] == 'o':
      if y1 == -1:
        y1 = i
        x1 = j
        continue
      else:
        y2 = i
        x2 = j
      
min_time = float('inf')

buttons = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def checkIsOut(y, x):
  if y < 0 or y >= n or x < 0 or x >= m:
    return True
  
  return False

def dfs(y1, x1, y2, x2, count):
  global min_time

  if(count >= 10):
    return

  count += 1
  for dy, dx in buttons:
    newY1 = y1+dy
    newX1 = x1+dx
    newY2 = y2+dy
    newX2 = x2+dx
  
    check1 = checkIsOut(newY1, newX1)
    check2 = checkIsOut(newY2, newX2)
  
    if(check1 ^ check2):
      min_time = min(min_time, count)
      return
    elif(check1 & check2):
      continue
    else:
      if(board[newY1][newX1] == '#'):
        newY1 = y1
        newX1 = x1
      if(board[newY2][newX2] == '#'):
        newY2 = y2
        newX2 = x2

      dfs(newY1, newX1, newY2, newX2, count)
      
    
dfs(y1, x1, y2, x2, 0)

if(min_time == float('inf')):
  print(-1)
else:
  print(min_time)