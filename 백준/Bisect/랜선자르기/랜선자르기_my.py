# k개의 길이가 다른 랜선을 가지고 있음
# k개의 랜선을 잘라서 n개의 같은 길이의 랜선으로 만들고자 함. 잘라낸 랜선은 다시 붙일 수 없음
# 만들 수 있는 최대 랜선의 길이

from bisect import bisect_left

f = open('./bisect/랜선자르기.txt', 'r')

k, n = map(int, f.readline().rstrip().split())

lans = []
for _ in range(k):
  lans.append(int(f.readline()))

total = sum(lans)

crnt =0
last = 0

k = n
while(True):
  last = crnt
  crnt = total//k
  
  count = sum([i//crnt for i in lans])
  k += 1
  
  if(count == n):
    break

maxLen = 0
for i in range(crnt, last):
  if sum([j//i for j in lans]) == n:
    maxLen = i

print(maxLen)

