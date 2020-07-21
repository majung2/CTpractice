# Mooyo Mooyo
# 탐색
# 2시간
# Gold 4

import sys
sys.setrecursionlimit(10000) 

N, K = map(int, input().split())
M = [[0]*12 for _ in range(N+2)]
ck = [] # 방문여부 확인
color = 0 # 색
size = 0 # 같은 색인 haybales 사이즈
s_count = 1 # process 반복 횟수를 위한 변수

# 데이터 입력
for i in range(1, N+1):
    data = list(input())
    for j in range(1, 11):
        M[i][j] = int(data[j-1])

# 방향벡터
dx, dy = [1,0,-1,0], [0,1,0,-1]

# 탐색
def dfs(x,y):
    global M, size, color
    ck[x][y] = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if M[xx][yy] == 0 or M[xx][yy]!=color or ck[xx][yy]:
            continue
        size+=1
        dfs(xx, yy)

# 0으로 바꾸기
def change(x,y):
    global M, color
    M[x][y] = 0
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if M[xx][yy] == 0 or M[xx][yy]!=color:
            continue
        change(xx,yy)

def gravity():
    global M, N
    A = [[0]*12 for _ in range(N+2)]
    for j in range(1,11):
        count = N
        for i in range(N, 0, -1):
            if M[i][j]!=0:
                A[count][j] = M[i][j]
                count-=1
    M = A

def process():
    global N, M, color, size, K, ck, s_count
    ck = [[0]*12 for _ in range(N+2)]
    s_count = 0
    for i in range(1,N+1):
        for j in range(1, 11):
            if M[i][j] == 0: 
                continue
            color = M[i][j] # 현재 색 확인
            size = 1 # 사이즈 초기화
            dfs(i,j)
            if size>=K:
                change(i,j)
                s_count+=1
    gravity()    

while s_count:
    process()

# M출력
for i in range(1,N+1):
    for j in range(1, 11):
        print(M[i][j],end='')
    print('')

# 인강풀이

def new_array(N):
    return [[0 for]]
    
N, K = map(int, input().split())
M = [list(input()) for _ inrange(N)]
ck = new_array()

while True:
    exist = True
    for i in range(N):
        for j in range(10):


    if exist:
        break

for i in range(N):
    print(''.join(i))

