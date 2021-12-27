import sys
sys.setrecursionlimit(10**5)

n = int(input())

tree = [[] for _ in range(n+1)]
parents = [0]*(n+1)

for _ in range(1, n):
  n, m = map(int, input().split())
  tree[n].append(m)
  tree[m].append(n)
  
def DFS(start, tree, parents):
  for i in tree[start]:
    if parents[i] == 0:
      parents[i] = start
      DFS(i, tree, parents)

DFS(1, tree, parents)

for i in parents[2:]:
  print(i)