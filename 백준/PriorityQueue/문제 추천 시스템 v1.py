from collections import defaultdict
import sys, heapq

ip = sys.stdin.readline

N = int(ip()) 

#문제번호 P, 난이도 L, 난이도가 어려운 순으로 정렬
easy = []
hard = []
solved = defaultdict(bool)

for _ in range(N):
  P, L = list(map(int, ip().split()))
  heapq.heappush(easy, [L, P])
  heapq.heappush(hard, [-L, -P]) #어려운 문제는 문제 번호가 큰 순


M = int(ip())
for _ in range(M):
  op = ip().split()
  
  if(op[0] == 'add'):
    P = int(op[1])
    L = int(op[2])
    while(solved[easy[0][1]]):
        heapq.heappop(easy)
    
    while(solved[-hard[0][1]]):
      heapq.heappop(hard)
    
    heapq.heappush(easy, [L, P])
    heapq.heappush(hard, [-L, -P]) #어려운 문제는 문제 번호가 큰 순
    
    solved[P] = False
    
  if(op[0] == 'recommend'):
    if(op[1] == '-1'):
      while(solved[easy[0][1]]):
        heapq.heappop(easy)
      print(easy[0][1])        
    
    if(op[1] == '1'):
      while(solved[-hard[0][1]]):
        heapq.heappop(hard)
      print(-hard[0][1])  

  if(op[0] == 'solved'):
    P = int(op[1])    
    solved[P] = True
    
