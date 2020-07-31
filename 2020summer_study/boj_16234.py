# 인구이동
# 시간초과
from sys import *
setrecursionlimit(10**4)

N, L, R = map(int, input().split()) 
answer = -1
A = [[0 for _ in range(N)] for _ in range(N)]
ck = [] # 갔던 곳인지 확인용
sum = {} # 연합별 인구수 합 {연합번호:[인구합,칸수]}

# 방향벡터
dx, dy = [1,0,-1,0], [0,1,0,-1]

for i in range(N): # 초기 인구 수 입력
    A[i] = list(map(int,input().split()))

def dfs(x,y,n):
    ck[x][y] = n # n번째 연합
    if n not in sum:
        sum[n] = [A[x][y],1] # 해당 연합의 첫번째 국가일 경우
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= N: # 벽을 만났을 때
            continue
        elif ck[xx][yy]: # 이미 방문한 나라
            continue
        elif abs(A[x][y]-A[xx][yy]) <= R and abs(A[x][y]-A[xx][yy]) >= L: # 범위에 포함되면
            sum[n][0] += A[xx][yy] # 인구수 추가
            sum[n][1] += 1 
            dfs(xx,yy,n)
# 인구이동
while(len(sum)<(N*N)): # 모든 국가가 각각 한 연합일 때 인구이동 끝남
    n = 1 # 연합
    sum = {} # 초기화
    ck = [[0 for _ in range(N)] for _ in range(N)] # 0으로 초기화
    for i in range(N):
        for j in range(N):
            if ck[i][j]:
                continue
            else:
                dfs(i,j,n)
                n+=1
    for i in range(N):
        for j in range(N):
            num = ck[i][j] # 연합번호
            A[i][j] = sum[num][0]//sum[num][1]
    answer += 1

print(answer)
