# 수 찾기
# Silver 4
# 20분

# 이분 탐색 > 딕셔너리 탐색


# N, A = int(input()), {i:1 for i in map(int, input().split())} 
# M, B = int(input()), list(map(int, input().split()))

# for i in B:
#     print(A.get(i,0))

# print(A)

# 인강풀이2
# set 활용

n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('1')
    else:
        print('0')