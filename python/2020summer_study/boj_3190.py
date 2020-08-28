# 뱀

N = int(input()) # 보드크기
K = int(input()) # 사과 개수

board = [[0 for _ in range(N)] for _ in range(N)] # 0 빈칸 1 사과 2 뱀
for _ in range(K):
    r, c= map(int, input().split())
    board[r-1][c-1] = 1

L = int(input()) # 뱀 방향변환 횟수
change_d = [0 for _ in range(L)]
for i in range(L):
    change_d[i] = list(map(str, input().split()))
    change_d[i][0] = int(change_d[i][0])

time = 0
snake = [[0,0]] # 뱀 좌표
board[0][0] = 2
dx, dy = [0,1,0,-1], [1,0,-1,0] # 우 하 좌 상
di = 0 # 방향 인덱스, 처음 오른쪽

next_turn = change_d.pop(0)
while(True):
    if next_turn[0] == time: # 방향전환 할 차례
        if next_turn[1] == 'L': # 왼쪽으로
            di = (di+3)%4
        elif next_turn[1] == 'D': # 오른쪽으로
            di = (di+1)%4
        if change_d: # 방향전환 남아있다면
            next_turn = change_d.pop(0)
        else: 
            next_turn = [10000,'X'] # 방향전환 끝

    xx, yy = snake[-1][0]+dx[di], snake[-1][1]+dy[di] # 다음에 갈 곳
    if xx >= N or xx < 0 or yy >= N or yy < 0: # 벽에 부딪힘
        time += 1
        break
    elif board[xx][yy] == 2: # 자기 몸에 부딪힘
        time += 1
        break
    elif board[xx][yy] == 1: # 사과가 있다면
        board[xx][yy] = 2 # 뱀 이동
        snake.append([xx,yy]) # 머리위치 바뀜
    else: # 사과 없다면
        board[xx][yy] = 2 # 머리이동
        snake.append([xx,yy])
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0
    time += 1
    
print(time)