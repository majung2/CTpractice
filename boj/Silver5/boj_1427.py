# 소트인사이드
# 하
# 정렬, 배열
# 8 / 25분

# N = int(input())
# li = []

# while N:
#     li.append(N%10)
#     N = N//10

# li.sort(reverse=True)

# result = 0
# while li:
#     result *= 10
#     result += li[0]
#     li.pop(0)

# print(result)

# 인강 풀이

array = input()

for i in range(9,-1,-1): # 9부터 0까지 1씩 작아지면서 반복
    for j in array:
        if int(j) == i:
            print(i, end='')



