# 퇴사

N = int(input()) # 남은 날짜

T, P = [0 for _ in range(N+1)], [0 for _ in range(N+1)]
maxMoney = 0

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

def dfs(day, money):
    global maxMoney
    if day > N: # 퇴사
        maxMoney = max(maxMoney, money)
        return
    # 이 날짜 선택
    if day+T[day]-1<=N:
        dfs(day+T[day], money+P[day])
    # 이 날짜 선택x
    dfs(day+1, money)

dfs(1,0)

print(maxMoney)
