# 수 정렬하기
# 하
# 정렬
# 29 / 15분
# Silver 5

N = int(input())
result = []

for _ in range(N):
    num = int(input())
    count = 0
    for i in range(len(result)):
        if num > result[i]:
            count+=1
        else:
            break
    if len(result) == 0:
        result = [num]
    else:
        result.insert(count,num)

for i in result:
    print (i)


