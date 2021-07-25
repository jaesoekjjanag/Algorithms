##색칠하기


def makeArray(arr, a, b, c, d, e):
    for i in range(a, c + 1):
        for j in range(b, d + 1):
            arr.append((i, j))
    return arr


n = int(input())
for k in range(n):
    arr1 = []
    arr2 = []
    m = int(input())

    for v in range(m):
        a, b, c, d, e = map(int, input().split())
        if e == 1:
            makeArray(arr1, a, b, c, d, e)
        if e == 2:
            makeArray(arr2, a, b, c, d, e)
    print("#{} {}".format(k + 1, len(set(arr1) & set(arr2))))
