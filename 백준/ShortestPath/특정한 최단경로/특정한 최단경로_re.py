import sys
from heapq import heappop, heappush 

# f = open('./input.txt')
# ip = f.readline
ip = sys.stdin.readline

n, e = map(int, ip().split())

graph = [[] for _ in range(n+1)]

for _ in range(e):
  a, b, c = map(int, ip().split())
  graph[a].append([c, b])
  graph[b].append([c, a])

u, v = map(int, ip().split())

# 1번에서 u와 v를 거쳐 n번까지 가는 최단 경로
# 1. 1 -> u -> v -> n
# 2. 1 -> v -> u -> n

def djikstra(start: int, dest: int)->int:
  dist = [float('inf')] * (n+1)
  dist[start] = 0
  
  heap = [[0, start]]
  
  while(heap):
    total_dist, cur = heappop(heap)
    
    for nxt_dist, nxt in graph[cur]:
      nxt_total_dist = total_dist + nxt_dist
      if(nxt_total_dist < dist[nxt]):
        dist[nxt] = nxt_total_dist
        heappush(heap, [nxt_total_dist, nxt])
  
  return dist[dest]

path1 = djikstra(1, u) + djikstra(u, v) + djikstra(v, n)
path2 = djikstra(1, v) + djikstra(v, u) + djikstra(u, n)

min_path = min(path1, path2)
print(-1 if min_path == float('inf') else min_path)