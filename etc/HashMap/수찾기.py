# n개의 정수 중 X라는 정수가 존재하는지 여부

import collections

n = int(input())
A = collections.Counter(map(int, input().split()))

m = int(input())
check_nums = map(int, input().split())

for i in check_nums:
  if A[i] >= 1:
    print(1)
  else:
    print(0)