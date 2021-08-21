def gcd_sub(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a + b  # while문이 끝난 이후엔 a또는 b 중 하나는 0이기 때문에 if 문으로 나누지 않고 더함


print(gcd_sub(3, 4))
