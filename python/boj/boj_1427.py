# 소트인사이드
# 하
# 정렬, 배열
# 8 / 25분

N = int(input())
li = []

while N:
    li.append(N%10)
    N = N//10

li.sort(reverse=True)

result = 0
while li:
    result *= 10
    result += li[0]
    li.pop(0)

print(result)



