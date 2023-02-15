f = open('./계단오르기.txt')
ip = f.readline

n = int(ip())

stairs = [int(ip()) for _ in range(n)]
if(n == 1):
  print(stairs[0])
  exit()
  
dp1 = [0]*n #2칸 연속
dp2 = [0]*n


dp1[0] = stairs[0]
dp2[0] = 0

dp1[1] = dp1[0] + stairs[1]
dp2[1] = stairs[1]

for i in range(2, n):
  dp1[i] = dp2[i-1] + stairs[i]
  dp2[i] = max(dp1[i-2], dp2[i-2]) + stairs[i]
  
print(max(dp1[n-1], dp2[n-1]))