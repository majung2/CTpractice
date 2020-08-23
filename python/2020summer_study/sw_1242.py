# 암호코드 스캔

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int, input().split())
    answer = 0

    code = [0 for _ in range(N)]:

    for i in range(N):
        code[i] = list(map(int, input().split()))

        

    print(f"#{test_case} answer")