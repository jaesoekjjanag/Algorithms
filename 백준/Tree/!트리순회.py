class Node:
  def __init__(self, value):
    self.value = value;
    self.left = None;
    self.right = None;


n = int(input())
tree = [0]*(2*n+1)

for i in range(n):
  tree[i] = Node(chr(i+65))

for i in range(n):
  N,L,R = map(ord,input().split())
  leftNode = tree[L-65]
  rightNode = tree[R-65]
  tree[N-65].left = leftNode
  tree[N-65].right = rightNode

def NLR(node):
  print(node.left, node.right)
  

NLR(tree[1])
