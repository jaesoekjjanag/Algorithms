import copy

def dfs(table, position, origin, n):
    length = len(table)
    result = [origin] 
    x, y = position
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    table[x][y] = -1
    
    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]
        if px < 0 or px >= length or py < 0 or py >= length or table[px][py] == n or table[px][py] == -1:
            continue
        
        table[px][py] = -1
        result += dfs(table, [px, py], [origin[0]+dx[i], origin[1]+dy[i]], n)

    return result
        

def rotate(arr):
    length = len(arr)
    rotated = [[0]*length for _ in range(length)]
    
    for i in range(length):
        for j in range(length):
            rotated[length-j-1][i] = arr[i][j]
            
    return rotated

def solution(game_board, table):
    length = len(game_board)
    spaces = []
    
    answer = 0
    
    # game_board에서 빈 공간 찾아서 spaces에 append
    for i in range(length):
        for j in range(length):
            if game_board[i][j] != -1 and game_board[i][j] == 0:
                spaces.append(dfs(game_board, [i, j], [0, 0], 1))
    
    for _ in range(4):
        table = rotate(table)
        table_copy = copy.deepcopy(table)
        
        for i in range(length):
            for j in range(length):
                if table[i][j] != -1 and table[i][j] == 1:
                    block = dfs(table_copy, [i, j], [0, 0], 0)
                    if block in spaces:
                        answer += len(block)
                        spaces.remove(block)
                        table = copy.deepcopy(table_copy)
                    else:
                        table_copy = copy.deepcopy(table)
    
    return answer

