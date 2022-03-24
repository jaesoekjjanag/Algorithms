A = [2,8,7,1,3,5,6,4]

# def quicksort(A, lo, hi):
#   def partition(lo, hi):
#     pivot = A[hi]
#     left = lo
#     for right in range(lo, hi):
#       if A[right] < pivot:
#         A[left], A[right] = A[right] , A[left]
#         left += 1
#     A[left], A[hi] = A[hi], A[left]
#     return left
  
#   if lo < hi:
#     pivot = partition(lo, hi)
#     quicksort(A, lo, pivot-1)
#     quicksort(A, pivot+1, hi)

def quick_sort(arr, left, right):
  if left >= right:
    return

  def partition(left, right):
    pivot = arr[right]
    i = left
    j = right-1
    
    while(i <= j):
      if arr[i] > pivot and arr[j] < pivot:
        arr[i], arr[j] = arr[j], arr[i]
      elif arr[i] > pivot:
        j -= 1
      elif arr[j] < pivot:
        i += 1
      else:
        i += 1
        j -= 1
    
    arr[i], arr[right] = arr[right], arr[i]
    return i
	
  pivot = partition(left, right)

  quick_sort(arr, left, pivot-1)
  quick_sort(arr, pivot+1, right)
  
quick_sort(A, 0, len(A)-1)
print(A)