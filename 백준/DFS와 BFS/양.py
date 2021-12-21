# .은 빈 필드, #은 울타리, o는 양, v는 늑대
# 양의 수가 늑대보다 많으면 늑대를 우리에서 쫓아낸다.
# 늑대의 수가 많으면 늑대가 양을 잡아먹는다.
# 아침이 되어 마당 안에 남은 양과 늑대의 수 

import sys
sys.setrecursionlimit(10**6)
r, c = map(int, input().split())
  
graph = []
for i in range(r):
  graph.append(list(input()))

sheepCount = 0
wolfCount = 0

def dfs(x, y, graph, counts):
  if(x >=0 and x < r and y>=0 and y < c):
    crnt = graph[x][y]
    if(crnt == '#'):
      return
    else:
      if(crnt == 'v'):
        counts[1] += 1
      elif(crnt == 'o'):
        counts[0] += 1
        
      graph[x][y] = '#'
      
      dfs(x-1, y, graph, counts)
      dfs(x+1, y, graph, counts)
      dfs(x, y-1, graph, counts)
      dfs(x, y+1, graph, counts)
  else:
    return

for i in range(r):
  for j in range(c):
    counts = [0,0]
    dfs(i, j, graph, counts)
    if(counts[0] > counts[1]):
      sheepCount += counts[0]
    else:
      wolfCount += counts[1]

print(sheepCount, wolfCount)


# r = 6
# c = 6

# graph = [['.', '.', '.', '#', '.', '.'],
#         ['.', '#', '#', 'v', '#', '.',],
#         ['#', 'v', '.', '#', '.', '#',],
#         ['#', '.', 'o', '#', '.', '#',],
#         ['.', '#', '#', '#', '.', '#',],
#         ['.', '.', '.', '#', '#', '#',]]