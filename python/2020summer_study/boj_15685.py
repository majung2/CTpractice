# 드래곤커브

N = int(input())
grid = [[0 for _ in range(101)] for _ in range(101)] # 격자
dx, dy = [1,0,-1,0], [0,-1,0,1] # 0: x좌표 증가  1: y좌표 감소  2: x좌표 감소  3: y좌표 증가
endPoint = [0,0] # 회전 기준점의 x, y 좌표

def turn(sPoint,bPoint): # sPoint 회전 기준점, bPoint 회전 시키려는 점
    sx, sy = sPoint[0], sPoint[1]
    bx, by = bPoint[0], bPoint[1]

    if sx==bx or sy == by:
        if sx - bx > 0 : # 0 -> 1
            return [sx, sy-(sx-bx)] 
        if sy - by < 0 : # 1 -> 2
            return [sx+(sy-by),sy]
        if sx - bx < 0 : # 2 -> 3
            return [sx, sy-(sx-bx)]
        if sy - by > 0: # 3 -> 0
            return [sx+(sy-by),sy]
    else: # 대각선 회전
        if sx - bx > 0 and sy - by < 0:
            return [sx+(sy-by),sy-(sx-bx)]
        if sx - bx > 0 and sy - by > 0:
            return [sx+(sy-by),sy-(sx-bx)]
        if sx - bx < 0 and sy - by > 0:
            return [sx+(sy-by),sy-(sx-bx)]
        if sx - bx < 0 and sy - by < 0:
            return [sx+(sy-by),sy-(sx-bx)]

for _ in range(N): 
    x, y, d, g = map(int,input().split())
    dragon = [[x,y]]
    endPoint = [x+dx[d],y+dy[d]] # 0세대 끝 점
    dragon.append(endPoint)

    while(g>0):
        temp = []
        for point in dragon:
            if point != endPoint:
                temp.append(turn(endPoint,point)) # 회전시켜 얻은 점 추가
        dragon += temp
        endPoint = turn(endPoint,[x,y])
        g -= 1

    for x,y in dragon: # 격자에 드래곤 커브 표시
        if x >= 0 and x <= 100 and y >=0 and y <= 100:
            grid[y][x] = 1

square = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] !=0 and grid[i+1][j] != 0 and grid[i][j+1]!=0 and grid[i+1][j+1]!=0:
            square += 1

print(square)