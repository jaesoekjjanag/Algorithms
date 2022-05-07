# 낱개 또는 6줄 패키지로 구입 가능.
# 최소 비용으로 N개의 기타줄을 구매하기 위해하는 법. 최소 비용 구하기
# 기타줄 브랜드 M개. 패키지가격과 낱개 가격

import sys


# f = open('기타줄.txt')
N, M = map(int, sys.stdin.readline().rstrip().split())
shops = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(M)]
# N, M = map(int, f.readline().rstrip().split())
# shops = [list(map(int, f.readline().rstrip().split())) for i in range(M)]

min_package = float('inf');
min_each = float('inf');

for package, each in shops:
  if(package < min_package):
    min_package = package
  if(each < min_each):
    min_each = each

result = min(N//6 * min_package + N%6*min_each, (N//6+1)*min_package, N*min_each) 
print(result)