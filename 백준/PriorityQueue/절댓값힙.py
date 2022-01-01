# 시간 초과한 내 풀이
# import heapq

# heap = []

# def pop():
#   if(len(heap) == 0):
#     print(0)
#     return
  
#   minus = []
#   for i in range(len(heap)):
#     if heap[i] < 0:
#       heap[i] *= -1
#       minus.append(heap[i])
      
#   heapq.heapify(heap)
#   minus.sort(reverse=True)
  
#   popped = heapq.heappop(heap)
  
#   if(popped in minus):
#     print(popped*-1)
#     minus.pop()
#   else:
#     print(popped)
    
#   for i in range(len(heap)):
#     if(len(minus) > 0 and heap[i] == minus[len(minus)-1]):
#       heap[i] *= -1
#       minus.pop()
  
# def push(value):
#   heapq.heappush(heap, value)
  
# n = int(input())

# for i in range(n):
#   op = int(input())
#   if(op == 0):
#     pop()
#   else:
#     push(op)


import heapq
import sys

heap = []

n = int(input())
for i in range(n):
  op = int(sys.stdin.readline())
  if(op == 0):
    if(not heap):
      print(0)
    else:
      print(heapq.heappop(heap)[1])
  else:
    heapq.heappush(heap,[abs(op), op])
