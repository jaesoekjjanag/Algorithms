from collections import deque

a, b = map(int, input().split())

MAX = 100000
visited = [0]*(MAX+1)
dist = [-1]*(MAX+1)

def bfs(s, d):
  Q = deque([s])
  visited[s] = 1
  dist[s] = 0

  while(Q):
    t = Q.popleft()

    if t==d:
      break;
    
    a = t-1
    if not visited[a] and a>=0:
      Q.append(a)
      visited[a] = 1
      dist[a] = dist[t] + 1
      
    b = t+1
    if not visited[b] and b <= MAX:
      Q.append(b)
      visited[b] = 1
      dist[b] = dist[t] + 1
      
    c = t*2
    if not visited[c] and c <= MAX: 
      Q.append(c)
      visited[c] = 1
      dist[c] = dist[t]

bfs(a, b)
print(dist[b])