# 에라토스테네스의 체

N, K = map(int, input().split())

decimal_ck = [1 for _ in range(N+1)] # 인덱스 값 = 숫자, 1: 남아있는거, 0: 지워진거
decimal_ck[0]=0
decimal_ck[1]=0
decimal = []

count = 0
answer = 0

while(count < N):
    p = decimal_ck.index(1)
    decimal.append(p)
    for i in range(N+1):
        if decimal_ck[i] == 0:
            continue
        elif i % p == 0:
            decimal_ck[i] = 0
            count += 1
            if count == K:
                answer = i
                break
    if answer > 0:
        break

print(answer)
