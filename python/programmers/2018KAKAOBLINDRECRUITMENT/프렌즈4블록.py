dx, dy = [0,1,1], [1,1,0] # 우 대각선 하
visit, remove_list, B = [], [], []
M, N = 0,0

def fall():
    global M, N, B
    for j in range(N):
        idx = M-1
        for i in range(M-1,-1,-1): # 밑에서부터 확인
            if B[i][j] == 0: # 빈칸이면
                if idx == M-1:
                    idx = i
                else:
                    continue
            else:
                B[idx][j]=B[i][j]
                if idx != i:
                    B[i][j]=0
                idx -= 1

def dfs(x, y):
    global remove_list, visit, B, M, N
    visit[x][y] = 0
    temp = B[x][y]
    if B[x+dx[0]][y+dy[0]] == temp and B[x+dx[1]][y+dy[1]] == temp and B[x+dx[2]][y+dy[2]] == temp:
        remove_list.append([x,y])
        if x+dx[0] < M-1 and y+dy[0] < N-1 and x+dx[1] < M-1 and y+dy[1] < N-1 and x+dx[2] < M-1 and y+dy[2] < N-1: 
            dfs(x+dx[0], y+dy[0])
            dfs(x+dx[1], y+dy[1])
            dfs(x+dx[2], y+dy[2])


def remove():
    global remove_list,B
    for x, y in remove_list:
        B[x][y] = 0
        B[x][y+1] = 0
        B[x+1][y+1] = 0
        B[x+1][y] = 0

def solution(m, n, board):
    global remove_list, check, visit, B, M, N
    answer = 0
    M, N = m, n
    B = [0 for _ in range(m)]
    for i in range(m):
        B[i] = list(board[i]) 

    while (True):
        visit = [[1 for _ in range(n)] for _ in range(m)] # 1안본거 0 본거
        change = 0
        for i in range(m-1):
            for j in range(n-1):
                if visit[i][j] and B[i][j]: # 값이 있다면
                    remove_list = []
                    dfs(i, j)
                    if remove_list:
                        remove()
                        change += 1
        if change == 0:
            break
        else:
            fall()

    for i in range(m):
        for j in range(n):
            if B[i][j] == 0:
                answer += 1
            
    return answer
