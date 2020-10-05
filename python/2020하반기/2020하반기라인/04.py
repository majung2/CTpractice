dx, dy = [0,1,0,-1], [1,0,-1,0] # 우 하 좌 상 

def solution(maze):
    answer = 0
    n = len(maze)
    x, y, d = 0, 0, 0 # 현재 위치, 얼굴 방향
    hx, hy = -1, 0 # 손을 대고 있는 좌표
    
    while(True):
        while(True): # 벽/미로끝
            xx, yy = x + dx[d], y + dy[d]
            if xx < 0 or xx >= n or yy < 0 or yy >= n: # 미로바깥
                hx, hy = xx, yy
                d = (d+1)%4
            elif maze[xx][yy]: # 벽이면
                hx, hy = xx, yy
                d = (d+1)%4
            else:
                break
        if hx+dx[d] < 0 or hx+dx[d] >= n or hy+dy[d] < 0 or hy+dy[d] >= n or maze[hx+dx[d]][hy+dy[d]]: # 직진
            hx, hy = hx+dx[d], hy+dy[d]
            x, y = xx, yy
            answer += 1
        else: # 벽 따라 회전: 손은 그대로, 방향은 반시계
            d = (d-1)%4
            x, y = xx+dx[d], yy+dy[d]
            answer += 2
        
        if x == n-1 and y == n-1:
            break
            
            
        
    return answer