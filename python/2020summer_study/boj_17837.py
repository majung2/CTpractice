# 새로운 게임2
from collections import deque

N, K = map(int, input().split())
Board = [[deque([]) for _ in range(N)] for _ in range(N)] # 모든 한칸은 모두 deque
B_color = [[0 for _ in range(N)] for _ in range(N)]
Mal = [0 for _ in range(K)]

dx, dy = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]

for i in range(N):
    B_color[i] = list(map(int, input().split()))

for i in range(K):
    x, y, d = map(int, input().split())
    x -= 1
    y -= 1
    Mal[i] = [x,y,d]
    Board[x][y].extend([i])

turn, fin = 1, False
while(turn <= 1000):
    for m in range(K): # m 번째 말 확인
        x, y, d = Mal[m][0], Mal[m][1], Mal[m][2]
        xx, yy = x+dx[d], y+dy[d] # 다음에 갈 위치
        if xx in [-1,N] or yy in [-1,N] or B_color[xx][yy] == 2: # 벽이나 파란색
            if d in [1,3]:
                d += 1
            else:
                d -= 1
            xx, yy = x+dx[d], y+dy[d]
        
        if xx in [-1,N] or yy in [-1,N] or B_color[xx][yy] == 2: # 또 벽 or 파
            xx, yy = x, y

        elif B_color[xx][yy] == 0 : # 흰색
            temp = deque()
            while(True): # m 가 나올 때까지 빼고
                t = Board[x][y].pop()
                temp.extend([t])
                Mal[t][0], Mal[t][1] = xx, yy
                if t == m:
                    break
            while(temp): # 다음꺼에 넣기
                t = temp.pop()
                Board[xx][yy].extend([t])
        else: # 빨간색
            while(True):
                t = Board[x][y].pop()
                Board[xx][yy].extend([t])
                Mal[t][0], Mal[t][1] = xx, yy
                if t == m:
                    break

        if len(Board[xx][yy]) >= 4: # 4개이상 쌓이면 게임 종료
            fin = True
            break
        Mal[m] = [xx,yy,d]

    if fin:
        break
    turn += 1

if turn > 1000:
    turn = -1
print(turn)