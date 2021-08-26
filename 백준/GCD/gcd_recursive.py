def gcd_re(a, b):
    if a == 0 and b == 0:
        return 0
    elif a == 0 or b == 0:
        print(max(a, b))
    else:
        if a > b:
            return gcd_re(a % b, b)
        else:
            return gcd_re(a, b % a)


gcd_re(12, 8)
