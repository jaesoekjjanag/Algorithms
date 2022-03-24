# 연결 리스트를 nlong에 정렬.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node4 = ListNode(3)
node3 = ListNode(1, node4)
node2 = ListNode(2, node3)
node1 = ListNode(4, node2)

# 병합 정렬
def solution(head):
  p = head
  lst = []
  while p:
    lst.append(p.val)
    p = p.next
    
  lst.sort()
  
  p = head
  for i in range(len(lst)):
    p.val = lst[i]
    p = p.next
    
  return head

print(solution(node1).val)