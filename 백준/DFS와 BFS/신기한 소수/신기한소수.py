N = int(input())
    
def isPrime(n):
  for i in range(2, int(n**0.5)+1):
    if n%i == 0:
      return False
    
  return True

def dfs(num):
    if len(str(num)) == N:
        print(num)
    else:
        for i in range(10):
            next = num * 10 + i
            if isPrime(next):
                dfs(next)

for i in [2, 3, 5, 7]:
  dfs(i)
