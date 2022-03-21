class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(6)
node7 = TreeNode(9)
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(7, node6, node7)
node1 = TreeNode(4, node2, node3)

def solution(root):
  def dfs(node):
    if not node:
      return
    
    node.left, node.right = node.right, node.left
    
    dfs(node.left)
    dfs(node.right)
    
  dfs(root)
  return

solution(node1)
