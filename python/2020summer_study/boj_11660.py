# 구간 합 구하기 5

N, M = map(int, input().split()) # N 표의크기, M 합 구하는 횟수
table = [[0 for _ in range(N)] for _ in range(N)]
loc = [0 for _ in range(M)]

for i in range(N):
    cur_line = list(map(int, input().split()))
    temp = 0
    for j in range(N):
        temp += cur_line[j]
        table[i][j] = temp
        if i != 0:
            table[i][j] += table[i-1][j]

for i in range(M):
    loc[i] = list(map(int, input().split()))

for case in loc:
    answer = 0
    x1, y1, x2, y2 = case[0]-1, case[1]-1, case[2]-1, case[3]-1
    
    answer += table[x2][y2]
    if x1 - 1 >= 0:
        answer -= table[x1-1][y2]
    if y1 -1 >= 0:
        answer -= table[x2][y1-1]
    if x1 -1 >=0 and y1 -1 >= 0:
        answer += table[x1-1][y1-1]
    print(answer)