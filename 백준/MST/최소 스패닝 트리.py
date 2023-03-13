import sys
f = open('./최소 스패닝 트리.txt')
input = f.readline

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
    
v, e = map(int, input().split())
parents = [i for i in range(v+1)]
answer = 0

edges = []
for _ in range(e):
  a, b, c = map(int, input().split())
  edges.append([c, a, b])

for c, a, b in sorted(edges):
  if(union(a, b, parents)):
    answer += c
    
print(answer)