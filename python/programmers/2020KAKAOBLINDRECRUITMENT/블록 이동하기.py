from collections import deque
dx, dy = [-1,0,1,0], [0,1,0,-1] # 상 우 하 좌

def solution(board):
    n = len(board) # board의 크기
    answer = 0 # 최소시간
    robot = [(0,0),(0,1)] # (n-1,n-1) 포함시 종료
    deq = deque([robot])

    while(True):
        current = deq.popleft()
        x1, y1, x2, y2 = current[0][0], current[0][1], current[1][0], current[1][1]

        if (n-1,n-1) in current:
            break

        else:
            answer += 1
            # 네 방향 가기
            for i in range(4): # 이미 갔던곳인지 확인 필요한가..?
                xx1, yy1, xx2, yy2 = x1+dx[i], y1+dy[i], x2+dx[i], y2+dy[i]
                if xx1 < 0 or xx1 >= n or yy1 < 0 or yy1 >= n or xx2 < 0 or xx2 >= n or yy2 < 0 or yy2 >= n: # 범위 밖
                    continue
                elif board[xx1][yy1] == 1 or board[xx2][yy2] == 1: # 벽
                    continue
                else:
                    deq.append([(xx1,yy1),(xx2,yy2)])

            # 네 방향 회전            
            for j in range(4):
                

            

















    return answer