#! R: 뒤집기, D: 버리기. 빈 배열에서 D를 사용하면 에러

from collections import deque
import sys

read = sys.stdin.readline

def solution():
    operators = read().rstrip()
    length = int(read().rstrip())
    arr = read().rstrip()[1:-1].split(",")
    if length == 0:
      arr = []
    
    arr = deque(arr)
    pointer = 0  #0일 때 popleft 1일 때 pop
    reverse_count = 0
    for o in operators:
      if o == 'R':
        pointer = 1 - pointer
        reverse_count += 1
        
      if o == 'D':
        if(not arr):
          return 'error'
        
        if(pointer == 0):
          arr.popleft()
        if(pointer == 1):
          arr.pop()

    if(reverse_count%2):
      arr.reverse()
      
    return '['+(','.join(arr))+']'
    
T = int(read())
for _ in range(T):
  print(solution())