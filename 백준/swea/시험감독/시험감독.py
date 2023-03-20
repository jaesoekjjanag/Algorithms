import sys, math
# input = sys.stdin.readline
input = open('./시험감독.txt').readline

n = int(input())
tester = list(map(int, input().split()))
main, sub = map(int, input().split())

answer = 0
for t in tester:
  answer += 1
  if(t > main):
    answer += math.ceil((t-main)/sub)

print(answer)