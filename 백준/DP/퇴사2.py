# N개의 T와 P가 주어짐. T는 상담의 소요일, P는 받을 수 있는 금액
# 받을 수 있는 최대 이익

f = open("퇴사2.txt")

n = int(f.readline().rstrip())
schedule = [[0, 0]]

for i in range(n):
  schedule.append(list(map(int, f.readline().rstrip().split())))

table = [0]*(n+2)

for i in range(1, n+1):
  t, p = schedule[i]
  table[i] = max(table[i], table[i-1])
  if(i+t-1 < n+1):
    table[i+t] = max(table[i] + p, table[i+t])

print(max(table))