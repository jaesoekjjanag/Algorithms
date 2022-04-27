from collections import defaultdict

f = open('트리.txt')

N = int(f.readline().rstrip()) #노드의 개수
tree_p = list(map(int, f.readline().rstrip().split())) # 각 노드의 부모
r = int(f.readline().rstrip()) #지울 노드

tree_v = [0]*N
root=-1

# key: 부모, value: 자식의 인덱스
tree = defaultdict(list)
for i in range(N):
  if tree_p[i] == -1:
    root = i
  else:
    tree[tree_p[i]].append(i)

def search_children(node):
  global tree_p;
  
  tree_v[node] = 1
  
  # i: 부모 노드가 node인 노드의 자식 노드 인덱스
  for i in tree[node]:
    if tree_v[i]:
      continue
    
    tree_v[i] = 1
    search_children(i) 

search_children(r)

count = 0
for i in range(N):
  if i not in tree:
    count += 1
  if len(tree[i]) == 1 and tree[i][0] == r:
    count += 1
    
print(count)