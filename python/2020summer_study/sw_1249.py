# 보급로

T = int(input())
Map = []

def enqueue(i,j,l):
    global cnt
    i[cnt] = i
    j[cnt] = j
    l[cnt] = l
    cnt += 1

def bfs(i,j):
    pos = 0
    global N

    enqueue(i,j,0) # 시작점 좌표정보, 시간정보 넣기

    while(pos < cnt && i[pos] is not N-1 || j[pos] is not N-1):
        









for test_case in range(1,T+1):
    N = int(input())
    Map = [0 for _ in range(N)]
    cnt = 0
    i, j, l = [0 for _ in range(N**2)], [0 for _ in range(N**2)], [0 for _ in range(N**2)]

    answer = 0 # 복구시간
    for i in range(N):
        Map[i] = list(map(int, list(input())))

    answer = bfs(0,0)

    print(f"#{test_case} {answer}")



