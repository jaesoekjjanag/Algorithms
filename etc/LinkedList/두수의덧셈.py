# 연결리스트의 역순의 합. 반환 값 역시 역순으로

from asyncio.windows_events import NULL


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node3 = ListNode(3)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

node6 = ListNode(4)
node5 = ListNode(6, node6)
node4 = ListNode(5, node5)

# 리스트로 만들고어서 합한뒤 다시 리스트로 분해. 그리고 연결 리스트로
def solution(l1, l2):
  n1 = []
  n2 = []
  
  node1 = l1
  node2 = l2
  
  while(node1 or node2):
    if node1:
      n1.append(node1.val)
      node1 = node1.next
    if node2:  
      n2.append(node2.val)
      node2 = node2.next
      
  
  sum = int(''.join(map(str, n1[::-1]))) + int(''.join(map(str, n2[::-1])))
  sum_list = list(str(sum))
  
  prev = None
  for i in sum_list:
    node = ListNode(i)
    node.next = prev
    prev = node
  
  return prev

solution(node1, node4)

# 숫자형 리스트를 reduce로 한번에 합치기

from functools import reduce

numbers = [1,2,3,4,5]
print(reduce(lambda x, y: 10*x + y, numbers))

