# 내 풀이 - 58점
# cityCount = int(input())
# distances = list(map(int, input().split()))
# stations = list(map(int, input().split()))

# answer = 0

# crnt = 0
# while(crnt <= len(distances)-1):
#   dest = crnt
#   for i in stations[crnt+1:]:
#     if(i < stations[dest]): 
#       dest = stations.index(i)
#       break
  
#   if(dest == crnt):
#     dest = len(stations)-1
  
#   distance = sum(distances[crnt:dest])
#   answer +=  distance* stations[crnt]
#   crnt = dest

# print(answer)

# 다른 사람의 풀이

cityCount = int(input())
distances = list(map(int, input().split()))
stations = list(map(int, input().split()))

answer = 0

min = stations[0]
for i in range(cityCount-1):
  if(stations[i] < min):
    min = stations[i]
  answer += min * distances[i]

print(answer)
  
