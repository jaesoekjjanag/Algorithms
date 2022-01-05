import os

path = os.getcwd()
f = open('회의실배정_test.txt', 'r')

n = int(f.readline())
meetings = []

for _ in range(n):
  start, end = map(int, f.readline().strip().split())
  meetings.append([end, start])
  
meetings.sort()

now = 0
answer = 0

for i in range(n):
  if(meetings[i][1] >= now):
    now = meetings[i][0]
    answer += 1

print(answer)    
