# import sys
# n, m = map(int, input().split())
# heights = list(map(int, input().split()))


f = open('나무자르기.txt')

n, m = map(int, f.readline().rstrip().split())
heights = list(map(int, f.readline().rstrip().split()))

left = 0
right = max(heights)

while(left <= right):
  mid = (left + right)//2
  result = mid
  s = sum([i-mid if i>mid else 0  for i in heights ])
  
  if s==m:
    print(mid)
    exit()
  if s>m:
    left = mid+1
  if s<m:
    right = mid-1
  
print(right)