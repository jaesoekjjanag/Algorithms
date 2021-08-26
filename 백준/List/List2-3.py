#이진탐색
#P:전체 페이지 Pa:A가 찾을 페이지 Pb: B가 찾을 페이지

def binarySearch(p, x):
  l = 1;
  r = p;
  counter = 0
  while l<r:
    c = int((l+r)/2);
    if c == x:
      print('answer')
      counter += 1
      return counter
    elif c > x:
      print(c)
      counter +=1
      r = c;
    elif c<x:
      print(c)
      counter +=1 
      l = c+1;
  return 0

T = int(input())
for _ in range(T):
  p, pa, pb = map(int, input().split())
  A = binarySearch(p, pa);
  B = binarySearch(p, pb);
  result =None;
  if (A>B):
      result = 'B'
  elif (A==B):
      result = '0'
  else:
      result = 'A'
  print('#{} {}'.format(_+1, result))
