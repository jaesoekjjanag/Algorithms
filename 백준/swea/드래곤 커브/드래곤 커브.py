import sys

# input = sys.stdin.readline
input = open('./input.txt').readline
n = int(input())

direction = [
  [1, 0],
  [0, -1],
  [-1, 0],
  [0, 1]
]
grid = [[0] * 101 for _ in range(101)]

def dragon_curve(y, x, d, g):
  grid[y][x] = 1
  conn = [d]
  
  for _ in range(g):
    grid[y][x] = 1
    
    for i in range(len(conn)-1, -1, -1):
      conn.append((conn[i]+1)%4)
  
  for i in range(len(conn)):
    y, x = y+direction[conn[i]][0], x+direction[conn[i]][1]
    if 0<=y<101 and 0<=x<101:
        continue
    grid[y][x] = 1

    

for _ in range(n):
  y, x, d, g = map(int, input().split())
  dragon_curve(y, x, d, g)
  
answer = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] and grid[i][j + 1] and grid[i + 1][j] and grid[i + 1][j + 1]:
            answer += 1
            
print(answer)