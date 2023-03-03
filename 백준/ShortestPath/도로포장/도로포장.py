from heapq import heappush, heappop
from collections import deque

f = open('./input.txt')
ip = f.readline

n, m, k = map(int, ip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b, c = map(int, ip().split())
  graph[a].append((c, b))
  graph[b].append((c, a))
  
def bfs(target: int, target_distance: int) -> list:
  dist = [-1] * (n+1)
  dist[target] = 0
  
  q = deque([target])
  result = []
  
  while(q):
    cur = q.popleft()
    
    for cost, nxt in graph[cur]:
      if(dist[nxt] != -1): continue
      
      nxt_dist = dist[cur] + 1
      if(nxt_dist < target_distance):
        q.append(nxt)
      if(nxt_dist == target_distance):
        result.append(nxt)
        
  return result

def djikstra(start: int, dest: int) -> int:
  dist = [float('inf')] * (n+1)
  dist[start] = 0
  
  heap = [(0, start)]
  
  while(heap):
    total_dist, cur = heappop(heap)
    
    if(dist[cur] < total_dist):
      continue
    
    for nxt_dist, nxt in graph[cur]:
      nxt_total_dist = total_dist + nxt_dist
      if(nxt_total_dist < dist[nxt]):
        dist[nxt] = nxt_total_dist
        heappush(heap, (nxt_total_dist, nxt))
  
  return dist[dest]

answer = 1000000
for dest in bfs(n, k):
  answer = min(answer, djikstra(1, dest))
  
print(answer) 
# print(max([djikstra(1, dest) for dest in bfs(n, k)]))
  
  
  
  
