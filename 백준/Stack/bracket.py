# () 또는 [] 괄호
# 모든 줄에서 괄호의 균형 검사
# .을 찍으면 종료


def bracket(p):
    stack = []
    try:
        for i in p:
            if i == ")" or i == "]":
                if (stack[-1] == "(" and i == ")") | (stack[-1] == "[" and i == "]"):
                    stack.pop()
                else:
                    return "no"
            if i == "(" or i == "[":
                stack.append(i)
        if len(stack) > 0:
            return "no"
        return "yes"
    except IndexError:
        return "no"


while True:
    p = input()
    if p == ".":
        break
    print(bracket(p))
