# 주어진 숫자 중 3가지 조합으로 M을 넘지 않는 최댓값을 만들기

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(i + 2, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum > M:
                continue
            else:
                result = max(result, sum)
print(result)
