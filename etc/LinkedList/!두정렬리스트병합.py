class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

nodeA3 = ListNode(4)
nodeA2 = ListNode(2, nodeA3)
nodeA1 = ListNode(1, nodeA2)

nodeB3 = ListNode(4)
nodeB2 = ListNode(3, nodeB3)
nodeB1 = ListNode(1, nodeB2)

def merge(l1, l2):
  if (not l1) or (l2 and l1.val > l2.val):
    l1, l2 = l2, l1
    
  if l1:
    l1.next = merge(l1.next, l2)
    
  return

merge(nodeA1, nodeB1)

  