n =5
nums = [-5, -2, -1, 1, 2, 4]

# n = int(input())
# nums = list(map(int, input().split()))
nums.sort()

lp = 0
rp = n-1

min_abs = float('inf')
result = [] 

while lp < rp:
    left = nums[lp]
    right = nums[rp]

    s = left + right
    if abs(s) < min_abs:
        min_abs = abs(s)
        result = [left, right]
	
    if s < 0:
        lp += 1
    else:
        rp -= 1

print(result[0], result[1])