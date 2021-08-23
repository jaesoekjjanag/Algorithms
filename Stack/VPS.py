def VPS(p):
    stack = []
    for _ in p:
        try:
            if _ == "(":
                stack.append(_)
            else:
                stack.pop()
        except IndexError:
            return "NO"
    if len(stack) > 0:
        return "NO"
    return "YES"


N = int(input())
for i in range(N):
    print(VPS(input()))
