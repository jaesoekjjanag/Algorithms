# N(짝수)명이 평일 오후에 모여서 축구.
# N/2명은 스타트 팀 남은 N/2명은 링크 팀

# S[i][j] + S[j][i]는 i와 j가 같은 팀에 속했을 때 팀에 더해지는 능력치
# 스타트 팀과 링크 팀의 능력치 차이의 최소 값

f = open('스타트와 링크.txt')

n = int(f.readline().rstrip())
s = [list(map(int, f.readline().rstrip().split())) for _ in range(n)]

min_sub = float('inf')

start = [0] * n

def cal_stat():
  global start
  global min_sub
  
  start_sum = 0
  link_sum = 0
  
  for i in range(n):
    for j in range(n):
      if start[i] and start[j]:
        start_sum += s[i][j]
        
      if not start[i] and not start[j]:
        link_sum += s[i][j]
      
  min_sub = min(min_sub, abs(start_sum - link_sum))


def recursion(index, len):
  global min_sub
  
  if len == n/2:
    cal_stat()
    return 
  
  for i in range(index, n):
    if start[i]:
      continue

    start[i] = 1
    recursion(i+1, len+1)
    start[i] = 0
    
recursion(0, 0)

print(min_sub)
