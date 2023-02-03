f = open('2048.txt')

# 5번 이동해서 얻을 수 있는 가장 큰 수

ip = f.readline
n = int(ip())
board = [list(map(int, ip().split())) for _ in range(n)]

def up():
  for i in range(n):
    for j in range(n-1, -1, -1):
      if(board[j][i] == 0): continue 
      
      if(board[j-1][i] == 0):
        board[j-1][i], board[j][i] = board[j][i], board[j-1][i]
        
      
      if(board[j][i] == board[j-1][i]):
        board[j-1][i] *= 2
        board[j][i] = 0
        i-=1
    
    for j in range(n):
      if(board[j][i] == 0):
        board[j]

def solution(N, number):
    dp = [0] + [set([int(str(N)*i)]) for i in range(1, 9)]
    
    for i in range(1, 9):
      for j in range(1, i):
        k = i - j
        for a in dp[j]:
          for b in dp[k]:
            dp[i].add(a+b)
            dp[i].add(abs(a-b))
            dp[i].add(a*b)
            if b != 0:
              dp[i].add(int(a//b))
      
      if number in dp[i]:
        return i
    
    return -1

print(solution(1, 30))