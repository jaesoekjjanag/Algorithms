import sys
ip = sys.stdin.readline

n, m = map(int, ip().rstrip().split())
nums = sorted(list(set(map(int, ip().rstrip().split()))))

def dfs(i, acc, l, nums):
  if(l == m):
    print(acc)
    return
  
  for j in range(i, len(nums)):
    num = nums[j]
    dfs(j, str(acc)+' '+str(num), l+1, nums)
  
for i in range(len(nums)):
  dfs(i, nums[i], 1, nums)