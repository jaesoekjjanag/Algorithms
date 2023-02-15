f = open('./피보나치함수.txt')

ip = f.readline
t = int(ip())

for _ in range(t):
  n = int(ip())
  
  dp = [0]*(n+2)

  dp[0] = [1, 0]
  dp[1] = [0, 1]

  for i in range(2, n+1):
    a1, b1 = dp[i-1]
    a2, b2 = dp[i-2]
    
    dp[i] = [a1+a2, b1+b2]

  z_count, o_count = dp[n]
  print(z_count, o_count)
