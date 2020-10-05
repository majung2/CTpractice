# 수들의 합2

N, M = map(int, input().split())

num = list(map(int, input().split()))

start, end = 0,1
answer =0

while(True):
    temp = sum(num[start:end])
    if temp == M:
        answer += 1
        start += 1
        end += 1
    elif temp > M:
        start += 1
    else:
        end += 1
    if end > N:
        break

print(answer)


    