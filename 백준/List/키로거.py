# f = open('./키로거.txt')
import sys

n = sys.stdin.readline().rstrip()

class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

for _ in range(int(n)):
  keyLog = sys.stdin.readline().rstrip()
  
  head = Node(None)
  tail = Node(None)
  head.next = tail
  tail.prev = head
  
  cur = head
  for k in keyLog:
    if k == '<':
      if cur != head:
        cur = cur.prev
    
    elif k == '>':
      if cur != tail.prev and cur != tail:
        cur = cur.next
    
    elif k == '-':
      if cur != head:
        prev = cur.prev
        next = cur.next
        
        prev.next = next
        next.prev = prev
        cur = prev
      
    else:
      #현재 커서와 그 다음 사이에 넣기
      newNode = Node(k)
      next = cur.next
      cur.next = newNode
      next.prev = newNode
      newNode.prev = cur
      newNode.next = next
      cur = newNode 
      
  cur = head.next
  while(cur.value):
    print(cur.value, end='')
    cur = cur.next
  
  print()
  
      
      