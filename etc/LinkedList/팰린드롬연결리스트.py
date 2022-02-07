class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node4 = ListNode(1)
node2 = ListNode(2, node4)
node1 = ListNode(1, node2)

#나의 풀이
def solution(node):
  crntNode = node
  values = []
  
  while(crntNode):
    values.append(crntNode.val)
    crntNode = crntNode.next
  
  
  # if len(values)%2 == 0:
  #   return values[:len(values)//2] == values[-1:len(values)//2-1:-1]
  # else:
  #   return values[:len(values)//2] == values[-1:len(values)//2:-1]
  lp = 0
  rp = len(values)-1
  
  while(lp <= rp):
    if values[lp] != values[rp]:
      return False
    lp += 1
    rp -= 1
    
  return True

# print(solution(node1))


# Deque를 이용한 풀이
from collections import deque
def isPalindrome(head):
  q = deque()
  
  if not head:
    return True
  
  node = head
  
  while node is not None:
    q.append(node.val)
    node = node.next
  
  while len(q) > 1:
    if q.popleft() != q.pop():
      return False
  
  return True

#! 런너 기법을 이용한 풀이.
def isPalindrome(head):
  rev = None
  slow = fast = head
  # fast는 두 칸씩 이동, 중간 지점까지 rev(노드의 역순)을 만들 수 있음.
  while fast and fast.next:
    fast = fast.next.next
    rev, rev.next, slow = slow, rev, slow.next
  
  # 홀수인 경우
  if fast:
    slow = slow.next
  
  # 중간까지의 역순(rev)와 중간 이후 부분을 비교하며 팰린드롬 확인
  while rev and rev.val == slow.val:
    slow, rev, = slow.next, rev.next
    print(slow, rev)    
  return not rev

print(isPalindrome(node1))