f = open('트리의지름.txt')

n = int(f.readline().rstrip())
tree = [[] for i in range(n+1)]

for i in range(n-1):
  a, b, c = map(int, f.readline().rstrip().split())
  tree[a].append([b, c])
  tree[b].append([a, c])
  
def dfs(node, distance):
  for b, c in tree[node]:
    if distances[b] == -1:
      distances[b] = distance + c
      dfs(b, distance + c)

# 지름의 한 끝
distances = [-1]*(n+1)
distances[1] = 0
dfs(1, 0)
end1 = distances.index(max(distances))

# 반대 쪽 지름의 끝
distances = [-1]*(n+1)
distances[end1] = 0
dfs(end1, 0)
diameter = max(distances)
print(diameter)


