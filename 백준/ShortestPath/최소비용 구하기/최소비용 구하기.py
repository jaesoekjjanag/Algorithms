from heapq import heappush, heappop
from collections import defaultdict

input = open('./input.txt').readline

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append([c, b])

start, dest = map(int, input().split())

def djikstra(start, dest):
  dist = [float('inf')]*1001
  dist[start] = 0
  q = [[0, start]]
  
  while(q):
    cost, node = heappop(q)
    
    for nxt_cost, nxt_node in graph[node]:
      nxt_cost = cost + nxt_cost
      if(nxt_cost < dist[nxt_node]):
        dist[nxt_node] = nxt_cost
        heappush(q, [nxt_cost, nxt_node])
        
  return dist[dest]

print(djikstra(start, dest))