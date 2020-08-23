# 게리맨더링 2

N = int(input()) # 재현시의 크기
A = [0 for _ in range(N+1)] # 인구수
B = [0,0,0,0,0] # 선거구별 인구수
answer = 40000
C = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
    temp = list(map(int, input().split())) 
    A[i] = [0]+temp


for d1 in range(1,N):
    for d2 in range(1,N-d1+1):
        for x in range(1,N-d1-d2+1):
            for y in range(1+d1, N-d2+1):
                if x+d1+d2 <=N and y+d2 <=N:
                    B = [0,0,0,0,0]
                    for r in range(1,N+1):
                        for c in range(1,N+1):
                            if r>=1 and r<x+d1 and c >=1 and c <= y: # 1번
                                B[0] += A[r][c]
                                C[r][c] = 1
                            elif r >=1 and r <= x+d2 and c > y and c <= N: # 2번
                                B[1] += A[r][c]
                                C[r][c] = 2
                            elif r >= x+d1 and r <= N and c >= 1 and c < y-d1+d2: # 3번
                                B[2] += A[r][c]
                                C[r][c] = 3
                            elif r > x+d2 and r <= N and c >= y-d1+d2 and c <= N: # 4번
                                B[3] += A[r][c]
                                C[r][c] = 4
                            else:
                                B[4] += A[r][c]
                                C[r][c] = 5


                    answer = min(answer, max(B) - min(B))

print(answer)



                


