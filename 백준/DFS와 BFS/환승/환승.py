from collections import defaultdict, deque
from sys import stdin

f = open('./환승.txt')
ip = f.readline
# ip = stdin.readline

n, k, m = map(int, ip().split())

station = defaultdict(list)
dist = [float("inf")] * (n+1)
dist[1] = 0

tube = defaultdict(list)
visited_tube = [0]*(m+1)

for t in range(1, m+1):
  linked = list(map(int, ip().split()))
  
  for s in linked:
    station[s].append(t)
    tube[t].append(s)

Q = deque([1])
while(Q):
  cur = Q.popleft()
  
  for t in station[cur]:
    if(visited_tube[t]): continue
    
    visited_tube[t] = 1
    for s in tube[t]:
      if(dist[s] == float('inf')):
        Q.append(s)
        dist[s] = dist[cur] + 1
        
print(- 1 if dist[n] == float('inf') else dist[n] + 1 )
