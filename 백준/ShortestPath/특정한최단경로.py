# 1부터 N까지 갈 때, v1과 v2를 지나면서 최단경로. 한 번 이동했던 경로로 다시 이동할 수 있음. 양방향 간선
from collections import defaultdict
import heapq
from math import inf
import sys

f = open("./특정한최단경로.txt")

N, E = map(int, f.readline().rstrip().split())

graph = defaultdict(list)
for _ in range(E):
  a, b, c = map(int, f.readline().rstrip().split())
  graph[a].append([c, b])
  graph[b].append([c, a])

v1, v2 = map(int, f.readline().rstrip().split());

def dijkstra(start, end):
    dis = [inf] * (N + 1)
    dis[start] = 0
    q = [[0, start]]
    while q:
        distance, node = heapq.heappop(q)
        # 아직 거리가 계산되지 않은 경우
        if distance <= dis[node]:
          for c, b in graph[node]: 
              if dis[b] > dis[node] + c:
                  dis[b] = dis[node] + c
                  heapq.heappush(q, [dis[b], b])

    return dis[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

min_path = min(path1, path2)
if min_path == inf:
  print(-1)
else:
  print(min_path)