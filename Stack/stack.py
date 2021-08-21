stack = []


def stackFunction(function, num=0):
    if function == "push":
        return stack.append(int(num))
    if function == "pop":
        for i in stack[::-1]:
            if type(i) == int:
                return i
        else:
            return -1
    if function == "size":
        count = 0
        for i in stack:
            if type(i) == int:
                count += 1
        return count
    if function == "empty":
        if len(stack) == 0:
            return 1
        else:
            return 0
    if function == "top":
        for i in stack[::-1]:
            if type(i) == int:
                return i
        return -1


N = int(input())
for i in range(N):
    order = [input().split(" ")]
    function = order[0]
    num = ""
    if len(order) == 2:
        num = order[1]
    print(stackFunction(function, num))
