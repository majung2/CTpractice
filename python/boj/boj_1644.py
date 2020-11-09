# 소수의 연속합
N = int(input())

# N보다 작은 소수들 모두 찾기

decimal = [] 

check = [0,0] + [1 for _ in range(N-1)]
for p in range(2, N+1):
    if check[p] == 0:
        continue
    else:
        decimal.append(p)
        for i in range(2 * p, N+1, p):
            check[i] = 0

# 경우의 수 구하기

start, count = len(decimal)-1, 1 # 시작 인덱스, 합할 갯수
answer = 0
while(True):
    if start > 0 and decimal[start-1] > N/count:
        start -= 1
    else:
        temp = sum(decimal[start:start+count])
        if temp == N:
            answer += 1
            start -= 1
            count += 1
        elif temp > N:
            start -= 1
        else:
            count += 1
        if start < 0:
            break
print(answer)
