#! 랜덤 순서임을 고려해서 다시 짜야함...

f = open('트리.txt')

N = int(f.readline().rstrip()) #노드의 개수
tree_p = list(map(int, f.readline().rstrip().split())) # 각 노드의 부모
r = int(f.readline().rstrip()) #지울 노드

def search_children(index):
  global tree_p;
  for j in range(index+1, N):
    v = tree_p[j]
    if v > index:
      break

    if v == index:
      search_children(j)
      
  tree_p[index] = -1

search_children(r)

count = 0
for i in range(N):
  if tree_p[i] == -1:
    continue
  
  if i not in tree_p[i+1:]:
    count += 1

print(count)