import sys
from heapq import heappop, heappush

f = open('./트리의 지름-1167.txt')
input = f.readline

v = int(input())

tree = [[] for _ in range(v+1)]
root = 1    

for _ in range(v):
  e = list(map(int, input().split()))
  v1 = e[0]
  
  for i in range(1, len(e)-1, 2):
    v2, dist = e[i], e[i+1]
    tree[v1].append([dist, v2])

answer = 0

#트리 지름 공식, 다익스트라를 사용한 방식
def getFarthestNode(node):
  dist = [float('inf')] * (v+1)
  dist[node] = 0
  Q = [[0, node]]
  while Q:
    cur_dist, cur_node = heappop(Q)
    if(cur_dist > dist[cur_node]):
      continue
    
    for nxt_dist, nxt_node in tree[cur_node]:
      acc_dist = cur_dist + nxt_dist
      if(dist[nxt_node] > acc_dist):
        dist[nxt_node] = acc_dist
        heappush(Q, [acc_dist, nxt_node])

  return max(enumerate(dist[1:], 1), key=lambda x: x[1])
  
node1 = getFarthestNode(1)[0]
answer = getFarthestNode(node1)[1]
print(answer)

# dfs를 이용한 방식: 메모리 초과
# from itertools import combinations

# def dfs(node, visited):
#   global answer
  
#   visited[node] = 1
#   max_dist = 0
#   sub_lens = []
#   for dist, children in tree[node]:
#     if(visited[children]): continue
#     sub_len = dist + dfs(children, visited)
    
#     sub_lens.append(sub_len)
#     max_dist = max(max_dist, sub_len)

#   if(len(sub_lens) > 1):
#     answer = max(answer, max(map(lambda x:sum(x), list(combinations(sub_lens, 2)))))
#   else:
#     answer = max(answer, max_dist)    
    
#   return max_dist

# dfs(root, [0]*(v+1))
# print(answer)
