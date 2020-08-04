# 구슬 탈출 2

N, M = map(int,input().split()) # 세로, 가로 3<= N, M <= 10
board = [0 for _ in range(N)]
Rloc, Bloc, Oloc = [0,0], [0,0], [0,0]
answer = 0

for i in range(N):
    board[i] = list(input())
    if 'R' in board[i]:
        Rloc=[i, board[i].index('R')]
    if 'B' in board[i]:
        Bloc=[i, board[i].index('B')]
    if 'O' in board[i]:
        Oloc=[i, board[i].index('O')]


di, dj = [-1,0,1,0],[0,1,0,-1]

def move(loc,n): # n은 방향 : 0상 1우 2하 3좌
    i, j =loc[0],loc[1]
    while(board[i+di[n]][j+dj[n]]=='.' or board[i+di[n]][j+dj[n]]=='O'): 
        i += di[n]
        j += dj[n]
        if board[i][j]=='O':
            break
    return [i,j]

for _ in range(10):
    answer += 1
    if move(Rloc,0) == Oloc or move(Rloc,1) == Oloc or move(Rloc,2) == Oloc or move(Rloc,3) == Oloc:
        break

print(answer)



