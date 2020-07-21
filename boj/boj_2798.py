# 블랙잭
# 배열, 완전탐색
# 20분
# Bronze 2

# N, M= map(int, input().split())
# cards= list(map(int, input().split()))

# maxSum = 0
# for i in range(N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             curSum = cards[i]+cards[j]+cards[k]
#             if curSum >M:
#                 continue
#             elif curSum > maxSum:
#                 maxSum = curSum

# print(maxSum)

# 인강코드

n, m = list(map(int, input().split()))
data = list(map(int, input().split()))

result = 0
length = len(data)
count = 0
for i in range(0,length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            sum_value = data[i]+data[j]+data[k]
            if sum_value <= m:
                result = max(result,sum_value)
print(result)

