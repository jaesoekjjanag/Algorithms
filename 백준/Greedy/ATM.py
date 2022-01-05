# i번 사람이 돈을 인출하는데 걸리는 시간은 Pi
# 모든 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

import sys

n = int(sys.stdin.readline())
p = list(map(int,sys.stdin.readline().split()))
p.sort()

for i in range(1,n):
    p[i] += p[i-1]

print(sum(p))

