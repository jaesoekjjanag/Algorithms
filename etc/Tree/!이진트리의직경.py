class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
node4 = TreeNode(4)    
node5 = TreeNode(5)    
node2 = TreeNode(2, node4, node5)
node3 = TreeNode(3)
node1 = TreeNode(1, node2, node3)

def diameter(node):
  longest_distance = 0
  
  def dfs(node):
    
    if node.left:
      left = dfs(node.left)
    if node.right:
      right = dfs(node.right)
      
    if not node.left and not node.right:
      node.val = 0
    else:
      node.val = max(left, right) + 1
    
    longest_distance = max(longest_distance, left + right + 2)
    return node.val
    
  print(longest_distance)
  
diameter(node1)