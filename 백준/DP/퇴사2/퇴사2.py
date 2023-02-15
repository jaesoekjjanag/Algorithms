f = open("퇴사2.txt")

n = int(f.readline().rstrip())
schedule = [[0, 0]]

for i in range(n):
  schedule.append(list(map(int, f.readline().rstrip().split())))

table = [0]*(n+2)

for i in range(1, n+1):
  t, p = schedule[i]
  table[i] = max(table[i], table[i-1])
  if(i+t-1 < n+1):
    table[i+t] = max(table[i] + p, table[i+t])

print(max(table))