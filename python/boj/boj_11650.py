# 좌표 정렬하기
# 하
# 정렬
# 15분

N = int(input())
array = []

for _ in range(N):
    x, y = map(int, input().split())
    array.append((x,y))
array = sorted(array) # 키를 이용하지 않아도 알아서 key=lambda x:(x[0], x[1])

for i in array:
    print(i[0],i[1])




