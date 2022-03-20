from collections import deque

tree = [3, 9, 20, None, None, 15, 7]

# 자식 노드의 index => 2*i + 1, 2*i + 2

def maxDepth(tree):
  q = deque([0])
  depth = 0
  
  while q:
    depth += 1
    
    print(q)
    for _ in range(len(q)):
      crnt_index = q.popleft()
      
      left = crnt_index*2+1
      right = crnt_index*2+2
      
      if left < len(tree):
        if tree[left]:
          q.append(left)
        if tree[right]:
          q.append(right)
        
  return depth

print(maxDepth(tree))