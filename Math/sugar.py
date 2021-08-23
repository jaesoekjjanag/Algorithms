# 3키로그램 봉지 or 5키로그램 봉지
# 최대한 적은 수의 봉지


from _typeshed import OpenTextModeUpdating


def sugar(n):
    five = n // 5
    if n % 5 == 0:
        return five
    for i in range(five, -1, -1):
        three = (n - i * 5) // 3
        rest = (n - i * 5) % 3
        if rest == 0:
            return i + three
    return -1


n = int(input())
print(sugar(n))
