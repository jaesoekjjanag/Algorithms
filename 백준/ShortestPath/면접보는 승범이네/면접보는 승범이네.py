from heapq import heappop, heappush
import sys

f = open('./input.txt')
ip = f.readline
# ip = sys.stdin.readline

n, m, k = map(int, ip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  u, v, c= map(int, ip().split())
  graph[v].append([c, u])

dist = [float('inf')] * (n+1)
heap = []

# 모든 면접 장소로 부터 동시에 탐색 시작
for s in map(int, ip().split()):
  dist[s] = 0
  heappush(heap, [0, s])

while(heap):
  total_dist, cur = heappop(heap)
  
  # total_dist: 여태까지 온 거리, dist[cur]: 해당 정점까지 최단 거리
  # 즉, dist[cur]이 더 작으면 이전에 구한 경로가 최단경로라는 뜻. 갱신할 필요 없다. 
  if(dist[cur] < total_dist):
    continue
  
  for nxt_dist, nxt in graph[cur]:
    nxt_total_dist = total_dist + nxt_dist
    if(nxt_total_dist < dist[nxt]):
      dist[nxt] = nxt_total_dist
      heappush(heap, [nxt_total_dist, nxt])

answer = [0, 0]
for i in range(1, n+1):
  val = dist[i]
  if val > answer[1]:
    answer = [i, val]
    
print(answer[0])
print(answer[1])
  