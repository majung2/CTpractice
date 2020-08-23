# 파티

N, M, X = map(int, input().split()) # N명 학생/마을, M개의 도로, X번 마을에서 파티
road = [[101 for _ in range(N+1)] for _ in range(N+1)] # T의 최댓값 100

temp = [0 for _ in range(N+1)]
fromX = [0 for _ in range(N+1)]
toX = [0 for _ in range(N+1)]
found = [False for _ in range(N+1)]

for _ in range(M): # 인접행렬
    r, c, t = map(int, input().split())
    road[r][c] = t
for i in range(N+1): # 대각선 0으로 초기화
    road[i][i] = 0

def find_min():
    global temp, found, N
    minn, minInx = 101, 0
    for i in range(1,N+1):
        if temp[i] < minn and found[i] == False:
            minn = temp[i]
            minIdx = i
    return minIdx

def shortest_from_X(start):
    global temp, found, road, N
    # 초기화
    for i in range(N+1):
        temp[i] = road[start][i]
        found[i] = False
    
    found[start] = True # 시작 정점 방문
    temp[start] = 0

    for _ in range(N-1):
        u = find_min()
        found[u] = True
        for w in range(1,N+1):
            if found[w] == False:
                temp[w] = min(temp[w], temp[u] + road[u][w])


shortest_from_X(X) # X로부터 가는 최단거리 찾기
fromX = temp[:]
# temp, found 초기화
temp = [0 for _ in range(N+1)]
found = [False for _ in range(N+1)]
# 간선 모두 반대로
for i in range(1,N+1):
    for j in range(1,i):
        road[i][j], road[j][i] = road[j][i], road[i][j]
shortest_from_X(X) # X까지 가는 최단거리 찾기
toX = temp[:]

answer = 0
for i in range(1,N+1):
    answer = max(answer, toX[i]+fromX[i])
print(answer)
