# Count Circle Groups

from sys import *
setrecursionlimit(10 ** 6)

T = int(input()) # 테스트케이스
dx, dy = [1,0,-1,0], [0,1,0,-1]

def dfs1(x, y, r, n): # 표시하는 것
    global H, W, armyBoard
    if r < n:
        return
    else:
        armyBoard[x][y] = 1
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx >= H or yy < 0 or yy >= W:
                continue
            else:
                dfs1(xx, yy, r, n+1)

def dfs2(x, y):
    global H, W, armyBoard
    if check[x][y]:
        return
    check[x][y] = 1
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx >= H or yy < 0 or yy >= W:
            continue
        elif armyBoard[xx][yy] == 0: # 빈 부분이면
            continue
        else:
            dfs2(xx,yy)


for _ in range(T):
    N = int(input())
    army = []
    answer, H, W = 0, 0, 0

    for i in range(N):
        x, y, R = map(int, input().split())
        H, W = max(H, x), max(W, y)
        army.append([x,y,R])

    H += 1
    W += 1
    armyBoard = [[0 for _ in range(W)] for _ in range(H)] # 빈 부분 -1
    check = [[0 for _ in range(W)] for _ in range(H)]


    for x,y,R in army:
        dfs1(x, y, R, 0)

    for x,y,R in army:
        if not check[x][y]:
            dfs2(x, y)
            answer += 1

    print(answer)