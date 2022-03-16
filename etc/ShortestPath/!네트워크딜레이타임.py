# K에서 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산. 모든 노드가 신호를 받지 못하면 -1 반환
# [출발지, 도착지, 소요시간] 

n = 4
k = 2

times=[[2,1,1],[2,3,1],[3,4,1]]

# 다익스트라 알고리즘

from collections import defaultdict
import heapq

def solution(times, n, k):
  graph = defaultdict(list)
  for u, v, w in times:
    graph[u].append((v, w))
    
  q = [(k, 0)]

  dist  = defaultdict(int)
  dist[k] = 0
    
  while q:
    node, distance = heapq.heappop(q)
    if not dist[node]:
      dist[node] = distance
      for v, w in graph[node]:
        heapq.heappush(q, (v, distance + w))

  if len(dist) < n:
    return -1
  else:
    return max(dist.values())
  
print(solution(times, n, k))