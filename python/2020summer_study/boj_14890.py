# 경사로

N, L = map(int, input().split())
Map = [[0 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
    Map[i] = list(map(int, input().split()))

for j in range(N): # 열 확인
    cur_h = Map[0][j]
    lk, hk = 0, 1 # 낮아지는 경사로, 높아지는 경사로
    flag = True
    for i in range(1,N):
        if Map[i][j] == cur_h:
            if lk!=0: # 낮경사로 놓는 중
                lk += 1
            else: # 높 경사로 놀수 있는 길이
                hk += 1
        elif abs(Map[i][j]-cur_h) > 1: # 1초과 차이면 안 됨
            flag = False
            break
        else:
            if Map[i][j]-cur_h<0: #낮 경사로
                if lk == 0: # 놓기시작
                    cur_h = Map[i][j]
                    lk += 1
                    hk = 0
                else: # 낮경사로 아직 안끝남
                    flag = False
                    break
            else: # 높 경사로
                if hk < L: # 경사로 놓을 수 없음
                    flag = False
                    break
                else: # 경사로 놓기
                    hk = 1
                    cur_h = Map[i][j]
        if lk == L: # 경사로 끝
            lk = 0  
    if lk > 0: # 낮경사로 범위 초과
        flag = False
    if flag:
        answer += 1

for i in range(N): # 행 확인
    cur_h = Map[i][0]
    lk, hk = 0, 1 # 낮아지는 경사로, 높아지는 경사로
    flag = True
    for j in range(1,N):
        if Map[i][j] == cur_h:
            if lk!=0: # 낮경사로 놓는 중
                lk += 1
            else: # 높 경사로 놀수 있는 길이
                hk += 1
        elif abs(Map[i][j]-cur_h) > 1: # 1초과 차이면 안 됨
            flag = False
            break
        else:
            if Map[i][j]-cur_h<0: #낮 경사로
                if lk == 0: # 놓기시작
                    cur_h = Map[i][j]
                    lk += 1
                    hk = 0
                else: # 낮경사로 아직 안끝남
                    flag = False
                    break
            else: # 높 경사로
                if hk < L: # 경사로 놓을 수 없음
                    flag = False
                    break
                else: # 경사로 놓기
                    hk = 1
                    cur_h = Map[i][j]
        if lk == L: # 경사로 끝
            lk = 0  
    if lk > 0: # 낮경사로 범위 초과
        flag = False
    if flag:
        answer += 1

print(answer)






