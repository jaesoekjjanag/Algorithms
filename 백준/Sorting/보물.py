f = open("보물.txt")

N = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))
B = list(map(int, f.readline().rstrip().split()))

S_A = sorted(A)
S_B = sorted(B, reverse=True)

result = sum([S_A[i]*S_B[i] for i in range(N)])
print(result)
