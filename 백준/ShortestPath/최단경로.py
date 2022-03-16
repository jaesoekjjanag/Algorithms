import sys
from collections import defaultdict
import heapq

V, E = map(int, sys.readline().rstrip().split()) #정점의 수, 간선의 수
k = int(sys.readline().rstrip()) #시작 정점
graph = defaultdict(list)

for _ in range(E):
  u, v, w = map(int, sys.readline().rstrip().split())
  graph[u].append((v, w))
  
dist = defaultdict(int)
q = [(0, k)]

while q:
  distance, node = heapq.heappop(q)
  if not dist[node]:
    dist[node] = str(distance)
    for v, w in graph[node]:
      heapq.heappush(q, (distance + w, v))
  
for i in range(1, V+1):
  if not dist[i]:
    print("INF")
  else:
    print(dist[i])