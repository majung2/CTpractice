# 이항 계수 2
# Silver 2

N, K = map(int, input().split())

answer = 1
K = min(K, N-K)


for _ in range(K):
    answer *= N
    N -= 1

for _ in range(K):
    answer //= K # 주의 /로 하면 틀림!!!
    K -= 1

answer %= 10007



print(int(answer))