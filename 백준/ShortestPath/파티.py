import sys
import heapq
from math import inf
from collections import defaultdict

f = open("./파티.txt")

# 플로이드 워셜 알고리즘으로 풀이. 시간 초과로 실패
# N, M, X = map(int, f.readline().rstrip().split()) 

# graph = [[inf]*(N+1) for _ in range(N+1)]

# for i in range(1, N+1):
#   for j in range(1, N+1):
#     if i==j:
#       graph[i][j] = 0
      
# for _ in range(M):
#   a, b, c = map(int, f.readline().rstrip().split())
#   graph[a][b] = c
  
# for k in range(1, N+1):
#   for i in range(1, N+1):
#     for j in range(1, N+1):
#       graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
      
# max_distance = 0
# for i in range(1, N+1):
#   max_distance = max(graph[i][X] + graph[X][i], max_distance)
  
# print(max_distance)


# 다익스트라 알고리즘 풀이
N, M, X = map(int, f.readline().rstrip().split()) 

graph = defaultdict(list)

for _ in range(M):
  a, b, c = map(int, f.readline().rstrip().split())
  graph[a].append([c, b])
  
def djikstra(start, end):
  global graph
  
  Q = [[0, start]]
  dist = [inf]*(N+1)
  dist[start] = 0
  
  while Q:
    time, node = heapq.heappop(Q)
    
    # c는 시간, b는 목적지
    if time > dist[node]:
      continue
    for c, b in graph[node]:
      if dist[b] > c + time:
        dist[b] = c + time
        heapq.heappush(Q, [c+time, b])
  
  return dist[end]

print(max([djikstra(i, X) + djikstra(X, i)  for i in range(1, N+1)]))