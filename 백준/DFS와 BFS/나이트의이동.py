from collections import deque
def bfs(end, start, graph, l):
  queue = deque([end])
  d = [[-1,2], [1,2], [2,1],[2,-1], [1,-2], [-1,-2],[-2,-1],[-2,1]]

  while(len(queue) > 0):
    task = queue.popleft();
    x = task[0];
    y = task[1];
    
    if(task == start):
      return graph[x][y]
    
    crnt = graph[x][y];
    for dx, dy in d:
      nextX = x+dx
      nextY = y+dy
      if( nextX >= 0 and nextY >=0 and nextX < l and nextY < l and graph[nextX][nextY] == 0):
        graph[nextX][nextY] = crnt + 1;
        queue.append([nextX, nextY]);

n = int(input())
for m in range(n):
  l = int(input())
  start = list(map(int, input().split()))
  end = list(map(int, input().split()))
  graph = []
  for i in range(l):
    graph.append([0 for i in range(l)])
  print(bfs(end, start, graph, l))



