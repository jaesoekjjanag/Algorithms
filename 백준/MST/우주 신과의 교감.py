import sys, math
# input = sys.readline
f = open('./우주 신과의 교감.txt')
input = f.readline

n, m = map(int, input().split())
def find(node: int, parents: list)->int:
  parent = parents[node]
  if(parent == node):
    return node
  
  return find(parent, parents)

def union(a:int, b:int, parents: list):
  a = find(a, parents)
  b = find(b, parents)

  if(a == b): return False
  
  if(a < b):
    parents[b] = a
  else:
    parents[a] = b
  
  return True

def distance(a, b):
  x1, y1 = a
  x2, y2 = b
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)
  
coord = [[]]+[list(map(int, input().split())) for _ in range(n)]
parents = [i for i in range(n+1)]
graph = []

for _ in range(m):
  a, b = map(int, input().split())
  union(a, b, parents)

for i in range(1, n):
  for j in range(i+1, n+1):
    graph.append((distance(coord[i], coord[j]), i, j))

graph.sort()

answer = 0
for dist, a, b in graph:
  if(union(a, b, parents)):
    answer += dist

print('{:.2f}'.format(round(answer, 2)))