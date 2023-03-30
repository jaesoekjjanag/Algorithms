stack = []
sum = 0
K = int(input())

for _ in range(K):
    a = int(input())
    if a == 0:
        pop = stack.pop()
        sum -= pop
    else:
        stack.append(a)
        sum += a
print(sum)
