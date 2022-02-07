class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

#재귀
# def reverse(node, prev=None):
#   if not node:
#     return prev
  
#   next = node.next
#   node.next = prev
#   return reverse(next, node)

# reverse(node1)

#반복
def reverse(head):
  crnt, prev =  head, None
  
  while(crnt):
    next = crnt.next
    crnt.next = prev
    prev = crnt
    crnt = next
    
  return prev
  
print(reverse(node1).val)