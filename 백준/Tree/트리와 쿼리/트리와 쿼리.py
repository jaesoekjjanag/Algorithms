import sys
input = sys.stdin.readline

n, r, q = map(int, input().split())
#q개의 정점 u들의 서브트리 개수


for _ in range(n-1):
  u, v = map(int, input().split()) #u와 v의 간선만으로 어느게 부모인지 어떻게 알까
  
  