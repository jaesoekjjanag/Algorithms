import sys
sys.setrecursionlimit(1000000)

n, k = map(int, input().split())

houses = []
for _ in range(n):
  houses.append(int(sys.stdin.readline()))

houses.sort()

start, end = 0, n-1

placed = [start, end]
k -= 2

def bisect(start, end):
  global k
  if(k > 0):
    midIndex = (start + end)//2
    placed.append(midIndex)
    k-=1
    
    leftIndex = (start+midIndex)//2 
    rightIndex = (midIndex+end)//2
    
    mid = houses[midIndex]
    left = houses[leftIndex]
    right = houses[rightIndex]
    
    leftMinSub = min(left - houses[start] , mid-left)
    rightMinSub = min(houses[end] - right , right-mid)
  
    if(leftMinSub > rightMinSub):
      bisect(start, midIndex-1)
      bisect(midIndex+1, end)
    else:
      bisect(midIndex+1, end)
      bisect(start, midIndex-1)

bisect(start, end)

print(placed)
placed.sort()

maxDistance = houses[end]-houses[start]
last = houses[0]

for i in placed[1:]:
  maxDistance = min(maxDistance, houses[i]-last)
  last = houses[i]
  
print(maxDistance)