from math import inf

f = open('./플로이드워셜.txt')

n = int(f.readline().rstrip())
m = int(f.readline().rstrip())

graph = [[inf]*(n+1) for _ in range(n+1)]
    
for _ in range(m):
  a,b,c = map(int, f.readline().rstrip().split())
  graph[a][b] = min(graph[a][b], c)    
  
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):import sys

n = int(input())
m = int(input())

graph = [[inf]*(n+1) for _ in range(n+1)]
    
for _ in range(m):
  a,b,c = map(int, sys.stdin.readline().split())
  graph[a][b] = min(graph[a][b], c)    
  
for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        graph[i][j] = 0
      else:
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == inf:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()

      if i == j:
        graph[i][j] = 0
      else:
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == inf:
      print(0, end=' ')
    else:
      print(graph[i][j], end=' ')
  print()
