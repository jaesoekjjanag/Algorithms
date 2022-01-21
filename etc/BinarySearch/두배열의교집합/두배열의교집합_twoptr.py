def intersection(nums1, nums2):
  intersect = set()
  
  nums1.sort()
  nums2.sort()
  
  ptr1 = 0;
  ptr2 = 0;
  
  while(ptr1 < len(nums1) and ptr2 < len(nums2)):
    n1 = nums1[ptr1]
    n2 = nums2[ptr2]
    if(n1 == n2):
      ptr1 += 1
      ptr2 += 1
      intersect.add(n1)
      
    elif(n1 > n2):
      ptr2 +=1
      
    else:
      ptr1 +=1 
  
  return intersect

print(intersection([1,2,2,1], [2,2]))