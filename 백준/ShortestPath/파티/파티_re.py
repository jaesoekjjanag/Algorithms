import sys
from heapq import heappop, heappush

ip = sys.stdin.readline
# f = open('./파티.txt')
# ip = f.readline

n, m, x = map(int, ip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  start, dest, time = map(int, ip().split())
  graph[start].append([time, dest])
  
def shortestPath(start: int, dest: int) -> int:
  dist = [float('inf')] * (n+1)
  dist[start] = 0
  
  heap = [[0, start]]
  
  while(heap):
    cur = heappop(heap)[1]
    cur_time = dist[cur]
    
    for [nxt_time, nxt] in graph[cur]:
      if(dist[nxt] > cur_time + nxt_time):
        dist[nxt] = cur_time + nxt_time
        heappush(heap, [dist[nxt], nxt])
  
  return dist[dest]

print(max([shortestPath(i, x) + shortestPath(x, i)  for i in range(1, n+1)]))

