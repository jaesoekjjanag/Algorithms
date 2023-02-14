import heapq, sys

f = open('./보석도둑.txt')

ip = f.readline
# ip = sys.stdin.readline

N, K = map(int, ip().split())

answer = 0
gems = []
bags = []

for _ in range(N):
  heapq.heappush(gems, list(map(int, ip().split())))

for _ in range(K):
  heapq.heappush(bags, int(ip()))

checked = []

while(bags):
  bag = heapq.heappop(bags)
  
  while(gems and gems[0][0] <= bag):
    gem = heapq.heappop(gems)
    heapq.heappush(checked, gem[1]*-1)
    
  if(checked):
    answer += heapq.heappop(checked) * -1
  
print(answer)