# 다리놓기
# Silver 5

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    answer = 1
    N = min(N, M-N)

    for _ in range(N):
        answer *= M
        M -= 1
    for _ in range(N):
        answer //= N
        N -= 1
    
    print(int(answer))


