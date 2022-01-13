import sys, os

f = open("./행렬곱셈_test.txt", "r")
arr = []

A = []
N, M = map(int, f.readline().rstrip().split())
for _ in range(N):
  A.append(list(map(int, f.readline().rstrip().split())))

B = []
M, K = map(int, f.readline().rstrip().split())
for _ in range(M):
  B.append(list(map(int, f.readline().rstrip().split())))

for n in range(N):
  for k in range(K):
    temp = 0
    for m in range(M):
      temp += A[n][m] * B[m][k]
    print(temp, end=' ')
  print()
    
