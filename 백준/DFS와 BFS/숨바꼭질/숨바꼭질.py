from collections import deque

def bfs(n, k):
  queue = deque()
  dist = [0]*(200000+1)
  queue.append(n)
  while(queue):
    task = queue.popleft()
    if(task == k):
      return dist[k]
    for i in (task*2, task+1,task-1):
      if(0<=i<200001 and dist[i] == 0 and i!=n):
        queue.append(i)
        dist[i] = dist[task] + 1
        

n, k = map(int, input().split())    
print(bfs(n,k))
  