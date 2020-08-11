# 격자판의 숫자 이어붙이기

T = int(input())
board = [0 for _ in range(4)]

dx, dy = [1,0,-1,0],[0,1,0,-1]
numbers = set()

for test_case in range(1,T+1):
    answer = 0
    for i in range(4):
        board[i] = list(map(int, input().split()))

    for i in range(4):
        for j in range(4):
            dfs(i,j)

















    print(f"#{test_case} {answer}")
    