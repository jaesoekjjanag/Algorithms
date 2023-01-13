n = int(input())

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

head = None
prev = None
for i in range(n):
  cur = Node(i)
  if not prev:
    head = cur
    
  prev.next = cur
  prev = cur
  
prev.next = head

cur = head
while(cur.value):
  one = cur.next
  two = cur.next.next

  one.next = two
  cur = two
  print(cur.value)

    