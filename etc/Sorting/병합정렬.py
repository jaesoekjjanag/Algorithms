def merge_sort(arr):
  if len(arr) < 2:
    return arr

  mid = len(arr)//2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  lp = rp = 0
  merged_arr = []
  while lp < len(left) and rp < len(right):
    if left[lp] < right[rp]:
      merged_arr.append(left[lp])
      lp += 1
    else:
      merged_arr.append(right[rp])
      rp += 1

  merged_arr.extend(left[lp:])
  merged_arr.extend(right[rp:])

  return merged_arr

print(merge_sort([3,1,8,2,5]))
