# 안전영역
# 런타임에러 > recursionlimit 필요
# 통과

from sys import *
setrecursionlimit(10 ** 6)

N = int(input()) # N차원 배열
H = [[0 for _ in range(N)] for _ in range(N)]
ck = [[0 for _ in range(N)] for _ in range(N)] # 갔는지 확인용
maxH, minH = 1, 100
answer = 1

dx, dy = [1,0,-1,0], [0,1,0,-1] # 방향벡터

for i in range(N):
    temp = list(map(int,input().split())) # 한 줄씩 입력
    maxH = max(temp) if max(temp) > maxH else maxH
    minH = min(temp) if min(temp) < minH  else minH
    H[i] = temp

def dfs(x,y,rain):
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i] # 다음갈 점
        if xx < 0 or xx >= N or yy < 0 or yy >= N: # 벽
            continue
        elif H[xx][yy] > rain and ck[xx][yy] == 0: # 물에 안 잠기고 안 갔던 곳
            dfs(xx,yy,rain)

for rain in range(minH,maxH):
    ck = [[0 for _ in range(N)] for _ in range(N)] # 체크 초기화 
    safe = 0
    for i in range(N):
        for j in range(N):
            if H[i][j] <= rain: # 물에 잠김
                ck[i][j] = 1
                continue
            elif ck[i][j] == 0: # 안 가본 곳
                dfs(i,j,rain)
                safe += 1
    answer = safe if safe > answer else answer

print(answer)