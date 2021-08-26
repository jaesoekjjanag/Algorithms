# 크기 N의 패턴: NxN의 정사각형 모양
# 크기 3일 때: 3x3이며 안에 공백이 있는 패턴

# def starRecursive(arg):
#   first = []
#   second =[]
#   third = []
#   init =''
#   if (arg == 1):
#     init = '*'
#   else:
#     init = starRecursive(arg-1)
#   for i in range(1, 4):
#     row = []
#     for j in range(1,4):
#       if (i ==2) & (j ==2):
#         row.append(' ')
#       else:
#         row.append(init)
#     if(i == 1):
#       first = row
#     elif(i ==2):
#       second = row
#     else:
#       third = row
#   return [first,second,third]


# result = starRecursive(1)

# def layout(arr):
#   res =[]
#   for i in arr:
#     res.append(''.join(i))
#   return res

# print(layout(result))

# def draw_star(n):
#   global Map

#   #n이 3일 때 1 또는 0으로 별 데이터 입력
#   if n == 3:
#     Map[0][:3] = Map[2][:3] = [1]*3
#     Map[1][:3] = [1,0,1]
#     return
#   #n이 3**2 이상일 때
#   a = n//3
#   draw_star(n//3)
#   # i:열
#   for i in range(3):
#     # i:행
#     for j in range(3):
#       if i == 1 and j ==1:
#         continue
#       for k in range(a):
#         #잘 모르겠음
#         Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]


# N = int(input())
# # Map: NxN의 2차원 배열
# Map =[[0 for i in range(N)] for i in range(N)]

# draw_star(N)

# for i in Map:
#   for j in i:
#     if j :
#       print('*', end ='')
#     else:
#       print(' ', end = '')
#   print()

# 행을 구분지어서 풀이
def append_star(LEN):
    if LEN == 1:
        return ["*"]

    # stars =[***, * *, ***]
    stars = append_star(LEN // 3)
    L = []
    # '*********', '* ** ** *', '*********'
    for S in stars:
        L.append(S * 3)
    for S in stars:
        L.append(S + " " * (LEN // 3) + S)
    for S in stars:
        L.append(S * 3)
    return L


print("".join(append_star(9)))

# 공간?을 넓히는 방식
def paint_star(LEN):
    DIV = LEN // 3
    if LEN == 3:
        g[1] = ["*", " ", "*"]
        g[0][:3] = g[2][:3] = ["*"] * 3
        return

    paint_star(DIV)

    for i in range(0, LEN, DIV):
        for j in range(0, LEN, DIV):
            if i != DIV or j != DIV:
                for k in range(DIV):
                    g[i + k][j : j + DIV] = g[k][:DIV]
