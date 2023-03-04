import sys

f = open('./input.txt')
ip = f.readline

n, m = map(int, ip().split())

graph = [[0 if i==j else float('inf')  for j in range(n+1)] for i in range(n+1)]
parent = [['-' for j in range(n+1)] for i in range(n+1)]

for _ in range(m):
  a, b, c = map(int, ip().split())
  graph[a][b] = c
  graph[b][a] = c
  
  parent[a][b] = b
  parent[b][a] = a

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j:
        graph[i][j] = 0
      else:
        if(graph[i][k] + graph[k][j] < graph[i][j]):
          graph[i][j] = graph[i][k] + graph[k][j]
          parent[i][j] = parent[i][k]
          

for i in range(1, n+1):
  for j in range(1, n+1):
    print(parent[i][j], end=' ')
    
  print()