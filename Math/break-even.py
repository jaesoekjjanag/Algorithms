# 고정비용 A만원 가변 비용 B만원
# 비용: A + nB

# 노트북 가격 C만원


def breakEven(A, B, C):
    if C <= B:
        return -1
    n = int(A / (C - B)) + 1
    return n


A, B, C = map(int, input().split())
print(breakEven(A, B, C))
