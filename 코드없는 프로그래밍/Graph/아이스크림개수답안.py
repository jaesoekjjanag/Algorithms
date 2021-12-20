def dfs(x, y):
  if(x <=-1 or x >= n or y<=-1 or y>=m):
    return False
  
  #visited set을 따로 두지 않고 1로 바꿈으로써 한번에 처리.
  if graph[x][y] == 0:
    graph[x][y] = 1
    
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
    


n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input())))

count =0;
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1
      
print(count);