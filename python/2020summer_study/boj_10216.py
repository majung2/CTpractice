# Count Circle Groups

from sys import *
setrecursionlimit(10 ** 4)

T = int(input()) # 테스트케이스
dx, dy = [1,0,-1,0], [0,1,0,-1]

def dfs1(x, y, r, n): # 표시하는 것
    global armyBoard
    if r < n:
        return
    elif (x,y) not in armyBoard:
        armyBoard[(x,y)] = 5001
    else:
        for i in range(4):
            xx, yy = x+dx[i], y+dy[i]
            if xx < 0 or xx > 5000 or yy < 0 or yy > 5000:
                continue
            else:
                dfs1(xx, yy, r, n+1)

def dfs2(x, y):
    global armyBoard
    if (x,y) not in armyBoard:
        return
    armyBoard.pop((x,y))
    for i in range(4):
        xx, yy = x+dx[i], y+dy[i]
        if xx < 0 or xx > 5000 or yy < 0 or yy > 5000:
            continue
        elif (xx, yy) not in armyBoard: 
            continue
        else:
            dfs2(xx,yy)


for _ in range(T):
    N = int(input())
    army = []
    answer = 0

    for i in range(N):
        x, y, R = map(int, input().split())
        army.append([x,y,R])

    armyBoard = {}

    for x,y,R in army:
        armyBoard[(x,y)] = R
        dfs1(x, y, R, 0)

    for x,y,R in army:
        if (x,y) in armyBoard: # 남아있음
            dfs2(x, y)
            answer += 1

    print(answer)