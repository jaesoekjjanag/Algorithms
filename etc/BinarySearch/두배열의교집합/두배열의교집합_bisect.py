from bisect import bisect_left

nums1 = [1,2,2,1]
nums2 = [2,2]


def intersection(nums1, nums2):
  intersect = set()
  nums2.sort()
  for i in nums1:
    j = bisect_left(nums2, i)
    if len(nums2) > 0 and len(nums2) > j and i == nums2[j]:
      intersect.add(i)
  return intersect

print(intersection(nums1, nums2))