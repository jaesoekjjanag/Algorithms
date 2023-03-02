from heapq import heappop, heappush
import sys

f = open('./input.txt')
ip = f.readline

n, m, k = map(int, ip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  u, v, c= map(int, ip().split())
  graph[u].append([c, v])

stations = list(map(int, ip().split()))

def djikstra(start: int, dest: int) -> int:
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

max_distance = 0
far = []

for i in range(1, n+1):
  for s in stations:
    distance = djikstra(i, s)
    if(distance > max_distance):
      print(distance, i, s)
      max_distance = distance
      far.append(i)

print(graph)
print(far)