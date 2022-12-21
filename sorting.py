import heapq

def quickSort(s):
  if len(s) <=1:
    return s
  
  p = s[0]
  left, mid, right = [], [], []
  
  for i in s:
    if i > p:
      right.append(i)
    if i < p:
      left.append(i)
    if i == p:
      mid.append(i)

  return quickSort(left) + mid + quickSort(right)

def selectionSort(s):
  length = len(s)
  
  for i in range(length):
    m = i
    for j in range(i, length):
      if s[j] < s[m]:
        m = j
        
    s[i], s[m] = s[m], s[i]
    
  return s

def insertionSort(s):
  length = len(s)
  
  for i in range(1, length):
    for j in range(i, 0, -1):
      if s[j-1] > s[j]:
        s[j-1], s[j] = s[j], s[j-1]
      else:
        break
  
  return s
        
def heapSort(s):
  heap = []
  for i in s:
    heapq.heappush(heap, i)
    
  result = []  
  while heap:
    result.append(heapq.heappop(heap))
    
  return result  


print(quickSort([3,1,2,8,6,4,10]))
print(selectionSort([3,1,2,8,6,4,10]))
print(insertionSort([3,1,2,8,6,4,10]))
print(heapSort([3,1,2,8,6,4,10]))
