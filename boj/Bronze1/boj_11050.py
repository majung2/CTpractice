# 이항 계수 1

N, K = map(int, input().split())

answer = 1

K = min(K, N-K)

for _ in range(K):
    answer *= N
    N -= 1

for _ in range(K):
    answer /= K
    K -= 1


print(int(answer))