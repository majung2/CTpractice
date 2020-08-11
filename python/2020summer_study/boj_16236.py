# 아기상어
from collections import deque

N = int(input()) # 공간의 크기
shark = [0,0] # 위치
fish = [[0 for _ in range(N)] for _ in range(N)]
check = [[0 for _ in range(N)] for _ in range(N)]

def bfs(): # 시작점 넣기
    global queue, fish, N, check

    time, size, eat_count = 0, 2, 0
    di, dj = [-1,0,0,1],[0,-1,1,0] # 상 좌 우 하

    while queue:
        temp = queue.popleft()
        i, j = temp[0], temp[1]
        for k in range(4):
            ii, jj = i + di[k], j + dj[k] # 다음 방문 점
            if ii < 0 or ii >= N or jj < 0 or jj >= N: # 벽일경우
                continue
            elif fish[ii][jj] > size: # 지나갈 수 없음
                continue
            elif fish[ii][jj] > 0 and fish[ii][jj] < size: # 먹을 수 있음
                fish[ii][jj] = 0 # 먹음
                eat_count += 1
                if eat_count == size:
                    eat_count = 0
                    size += 1
                shark = [ii,jj] # 상어 움직임
                time += check[i][j]
                queue = deque([shark]) # 새로운 위치에서 시작
                check = [[0 for _ in range(N)] for _ in range(N)] # 초기화
                check[ii][jj] = 1
                break
            elif check[ii][jj] == 0: # 지나갈 때 (안 갔던 곳만)
                check[ii][jj] = check[i][j]+1
                queue.append([ii,jj])
    return time


for i in range(N):
    temp = list(map(int, input().split()))
    fish[i] = temp
    if 9 in temp:
        j = temp.index(9)
        shark = [i,j]
        fish[i][j] = 0

check[shark[0]][shark[1]] = 1
queue = deque([shark])
print(bfs())