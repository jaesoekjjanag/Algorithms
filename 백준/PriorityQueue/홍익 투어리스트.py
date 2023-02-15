import sys, bisect

f = open('./홍익 투어리스트.txt')

ip = f.readline;

N, Q = map(int, ip().split())
areas = list(map(int, ip().split()))

hot_places = set([i for i, v in enumerate(areas) if v == 1])

location = 0 

for _ in range(Q):
  query = list(map(int, ip().split()))
  if(query[0] == 1):
    i = query[1]-1
    if(areas[i]==1):
      hot_places.remove(i)
    else:
      hot_places.add(i)
      
    areas[i] = 1-areas[i]
  
  if(query[0] == 2):
    location = (location + query[1]) % N
    
  if(query[0] == 3):
    if(not hot_places):
      print(-1)
    else:    
      h = list(hot_places)
      i = bisect.bisect_left(h, location)
      if(i == len(hot_places)):
        print(h[0] + N - location)
      else:
        print(h[i] - location)
