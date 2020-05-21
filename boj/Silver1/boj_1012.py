# 유기농 배추
# 탐색
# 인강풀이

import sys
sys.setrecursionlimit(10000) # 재귀함수 깊이를 제한

T = int(input()) # 테스트 케이스
B, ck =[], [] # B 배추 ck 갔던 곳

# 방향벡터!!
dx, dy = [1,0,-1,0], [0,1,0,-1] #우 하 좌 상


def dfs(x, y):
    global B, ck
    ck[x][y] = 1 # 처음에 체크하고 
    for i in range(4): # 네 방향 확인
        xx, yy = x + dx[i], y + dy[i] # xx, yy 다음에 돌 점
        if B[xx][yy] == 0 or ck[xx][yy] :
            continue
        dfs(xx, yy)


def process():
    global B, ck
    M, N, K = map(int, input().split()) # 배추밭 가로, 세로, 배추 위치
    B = [[0 for i in range(M+2)] for _ in range(N+2)] # 상하좌우 1칸씩 추가
    ck = [[0 for i in range(M+2)] for _ in range(N+2)] # 상하좌우 1칸씩 추가
    for _ in range(K):
        X, Y = map(int, input().split())
        B[Y+1][X+1] = 1

    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if ck[i][j]: 
                continue
            if B[i][j]:
                dfs(i, j)
                ans += 1

    print(ans)

for _ in range(T):
    process()


    




