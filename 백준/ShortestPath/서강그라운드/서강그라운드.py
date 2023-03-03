import sys
from heapq import heappop, heappush

ip = open('./input.txt').readline

n, m, r = map(int, ip().split())
items = list(map(int, ip().split()))

dist = [[0 if(i==j) else float('inf') for j in range(n+1)] for i in range(n+1)]

for _ in range(r):
  a, b, c  = map(int, ip().split())
  dist[a][b] = c
  dist[b][a] = c
  
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])      

answer = 0
for i in range(1, n+1):
  temp = 0
  for j in range(1, n+1):
    distance = dist[i][j]    
    if(distance <= m):
      temp += items[j-1]
      
  answer = max(answer, temp)

print(answer)

