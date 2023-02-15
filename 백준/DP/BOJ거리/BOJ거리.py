# 항상 큰 번호로 점프
# k칸 점프하는데 필요한 에너지는 k^2
# B O J 순서로 이동
# N번까지 가는데 필요한 최소 비용 

f = open("BOJ거리.txt")

n = int(f.readline().rstrip())
street = f.readline().rstrip()

def good2go(crnt, next):
  d = {'B': 'O', 'O': 'J', 'J':'B'}
  return d[crnt] == next


dp = [float('inf') for i in range(n)]
dp[0] = 0

for i in range(n):
  crnt = street[i]
  for j in range(i+1, n):
    next = street[j]
    if good2go(crnt, next):
      dp[j] = min(dp[j], dp[i] + (j-i)**2)

if dp[n-1] == float('inf'):
  print(-1)
else:
  print(dp[n-1])
