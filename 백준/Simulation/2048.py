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
        