# 치킨배달
from collections import deque

N, M = map(int, input().split()) # N 도시크기, M 최대 치킨집 수
city = [0 for _ in range(N)]
chicken_count = 0
chicken, house = [],[] # 치킨집 위치, 집 위치
remove = []
dx, dy = [-1,0,1,0], [0,1,0,-1] # 상 우 하 좌

for i in range(N): # 입력
    city[i] = list(map(int, input().split()))
    for j in range(N):
        if city[i][j] == 1: # 집
            house.append([i,j])
        elif city[i][j] == 2: # 치킨집
            chicken.append([i,j])
            chicken_count += 1

# 가장 가까운 집/치킨집 거리 찾기
def findCloset(x,y,t): # 좌표, type(집/치킨집)
    global N, city
    find = t%2+1
    queue = deque([[x,y]]) 
    while queue:
        temp = queue.popleft()
        i, j = temp[0],temp[1]
        for k in range(4):
            ii, jj = i+dx[k], j+dy[k]
            if ii < 0 or ii >= N or jj < 0 or jj >= N:
                continue
            elif city[ii][jj] == find: # 찾음
                return abs(x-ii)+abs(y-jj)
            else:
                queue.append([ii,jj])

def chickenway(N): # 치킨거리 구하는 함수
    global house
    dis = 0
    for h in house:
        dis += findCloset(h[0],h[1],1)
    return dis 

if chicken_count > M:
    for c in chicken: 
        dis1 = findCloset(c[0],c[1],2)
        dis2, cnt = 0, 0
        for h in house: # 모든 집과의 치킨거리 계산
            if dis1 == abs(c[0]-h[0])+abs(c[1]-h[1]):
                cnt += 1
            dis2 += abs(c[0]-h[0])+abs(c[1]-h[1])
        remove.append((dis1,cnt,dis2,c))
    remove = sorted(remove, key=lambda x: (-x[0],x[1],-x[2]))

for i in range(chicken_count-M):
    rm_loc = remove[i][3]
    city[rm_loc[0]][rm_loc[1]] = 0

print(chickenway(N))