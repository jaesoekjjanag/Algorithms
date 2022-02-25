import collections
import heapq


nums = [1,1,1,2,2,3]
k = 2

def solution1(nums, k):
  freq = collections.Counter(nums)
  freq_heap = []
  
  for f in freq:
    heapq.heappush(freq_heap, (-freq[f], f)) #파이썬의 heap은 최소 힙만 지원하기 때문에, 가장 큰 값의 우선순위를 높일 수 있또록 (-)를 붙여준다.
  
  result = []
  for _ in range(k):
    result.append(heapq.heappop(freq_heap)[1])
    
  return result


def solution2(nums, k):
  return list(zip(*collections.Counter(nums).most_common(2)))[0] # (*)를 앞에 붙이면 list를 언팩한다.
  
print(solution2(nums, k))