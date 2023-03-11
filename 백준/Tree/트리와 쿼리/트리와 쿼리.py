import sys
sys.setrecursionlimit(10**7)

# input = sys.stdin.readline
input = open('./트리와 쿼리.txt').readline

n, r, q = map(int, input().split())

tree = [[] for _ in range(n+1)]
subtree_count = [0]*(n+1) 
visited = [0]*(n+1)

def traverse(node, visited):
  visited[node] = 1
  count = 1
  
  for children in tree[node]:
    if(not visited[children]):
      count += traverse(children, visited)
  
  subtree_count[node] = count
  return count

for _ in range(n-1):
  u, v = map(int, input().split()) 
  tree[u].append(v)
  tree[v].append(u)
  
traverse(r, visited)

for node in range(q):
  print(subtree_count[int(input())])

