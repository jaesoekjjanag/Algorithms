# 입력받은 연결리스트를 두개씩 스왑

from email import header


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# 값만 교환
def solution(head):
  cur = head
  
  #! 다음 node와 값을 교환한 뒤에 두칸 건너 뛴다.
  while cur and cur.next:
    cur.val, cur.next.val = cur.next.val, cur.val
    cur = cur.next.next
  
  return head

# 재귀