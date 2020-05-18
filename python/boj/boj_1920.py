# 수 찾기

# 이분 탐색 > 딕셔너리 탐색


N, A = int(input()), {i:1 for i in map(int, input().split())} 
M, B = int(input()), list(map(int, input().split()))

for i in B:
    print(A.get(i,0))

print(A)