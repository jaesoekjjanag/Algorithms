#부분집합 구하기
r = int(input())

for _ in range(r):
    A = list(range(1,13))
    n= len(A)
    count = 0

    N,K = map(int, input().split())

    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(A[j])
        if (sum(subset) == K and len(subset)==N):
            count+=1
    print('#{} {}'.format(_+1, count))



