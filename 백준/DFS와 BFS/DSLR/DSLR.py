# import sys
from collections import deque

f = open('dslr.txt')

n = int(f.readline().rstrip())
T = [list(map(int, f.readline().rstrip().split())) for _ in range(n)]


def dslr(num, op):
  if op == 'D':
    num *= 2
    return num%10000
  
  if op == 'S':
    if num == 0:
      return 9999
    return num-1
  
  if op == 'L':
    return num%1000*10+num//1000
    
  if op == 'R':
    return num%10*1000+num//10


def bfs(a, b):
  visited = [0]*10000
  
  Q = deque()
  Q.append([a, ''])
  visited[a] = 1
  
  while Q:
    task, ops = Q.popleft()
    if task == b:
      return ops
    
    for op in ['D', 'S', 'L', 'R']:
      t = dslr(task, op)
      if visited[t]:
        continue
      
      newOp = ops + op
      visited[t] = 1
      Q.append([t, newOp])
    

for a, b in T:
  print(bfs(a, b))
  