# 진법 별 자릿수 곱 최대

def turn(j, N):
    k = 1
    while(N):
        if N%j != 0:
            k *= (N%j)
        N //= j
    return k
def solution(N):
    answer = []
    j, k = 2, 0

    for i in range(2, 10):
        if turn(i, N) >= k:
            j, k = i, turn(i, N)
    
    answer = [j, k]
    return answer