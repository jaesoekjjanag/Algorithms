class CircularQueue:
  def __init__(self, k):
    self.q = [None]*k;
    self.maxlen = k;
    self.front = 0;
    self.rear = 0;
    
  def enQueue(self, n):
    if self.q[self.rear] == None:
      self.q[self.rear] = n;
      self.rear = (self.rear+1) % self.maxlen;
      return True
    
    else:
      return False
    
  def deQueue(self):
    if self.q[self.front] == None:
      return False
    else:
      self.q[self.front] = None
      self.front += (self.front+1) % self.maxlen;
      return True
    
  def getFront(self):
    if self.q[self.front]:
      return self.q[self.front]
    else:
      return -1
    
  def getRear(self):
    if self.q[self.rear-1]:
      return self.q[self.rear-1]
    else:
      return -1
    
  def isEmpty(self):
    if self.front == self.rear and self.q[self.front] == None:
      return True
    else:
      return False
    
  def isFull(self):
    if self.front == self.rear and self.q[self.front] != None:
      return True
    else:
      return False
  
  
cq = CircularQueue(5)
print(cq.enQueue(1))
print(cq.enQueue(2))
print(cq.enQueue(3))
print(cq.enQueue(4))
print(cq.enQueue(5))
print(cq.enQueue(6))
print(cq.getFront())
print(cq.getRear())
print(cq.deQueue())
print(cq.getFront())