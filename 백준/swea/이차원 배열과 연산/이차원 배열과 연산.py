from collections import Counter
from functools import reduce
input = open('./input.txt').readline

r, c, k = map(int, input().split())

# A[r][c] == k가 되기 위한 최소 시간
A = [list(map(int, input().split())) for _ in range(3)]

def calc(arr):
  counter = Counter(arr)
  return reduce(lambda acc, x: acc + list(x), sorted(list(counter.items()), key=lambda x: (x[1], x[0])), [])

def R(arr):
  for i in range(len(arr)):
    arr[i] = calc(arr[i])

def C(arr):
  arr = [list(a) for a in zip(*arr)]
  R(arr)
  arr = [list(a) for a in zip(*arr)]

answer = 0
while(True):
  if A[r][c] == k:
    print(answer)
    break
  else:
    if(len(A) < len(A[0])):
      C(A)
    else:
      R(A)
  
