f = open('상근이의 여행.txt')

t = int(f.readline().rstrip())

for _ in range(t):
  n, m = map(int, f.readline().rstrip().split())
  
  for _ in range(m):
    a, b = map(int, f.readline().rstrip().split())

  print(n-1)