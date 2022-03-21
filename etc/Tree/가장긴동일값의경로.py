class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
node7 = TreeNode(4)
node4 = TreeNode(4, node7)
node5 = TreeNode(4)
node6 = TreeNode(5)
node2 = TreeNode(4, node4, node5)
node3 = TreeNode(5, None, node6)
node1 = TreeNode(1, node2, node3)

longest = 0
def solution(root):
  global longest
  def dfs(node):
    global longest
    if not node:
      return 0
    
    left = dfs(node.left)
    right = dfs(node.right)
    
    if node.left and node.left.val == node.val:
      left += 1
    else:
      left = 0
      
    if node.right and node.right.val == node.val:
      right += 1
    else:
      right = 0

    longest = max(longest, left + right)
    return max(left, right)
  
  dfs(root)
  return longest

print(solution(node1))