def solution(N, stages):
    not_clear = [0 for _ in range(N+2)] # 인덱스 = 스테이지 넘버
    stage_arrive = [0 for _ in range(N+1)]
    fail = {}


    for stage in stages:
        not_clear[stage] += 1
    
    for i in range(N, 0, -1):
        if i == N:
            stage_arrive[i] = not_clear[i+1]+not_clear[i]
        else:
            stage_arrive[i] = not_clear[i]+stage_arrive[i+1]

    for i in range(1,N+1):
        if stage_arrive[i]:
            fail[i] = not_clear[i]/stage_arrive[i]
        else:
            fail[i] = 0

    return sorted(fail, key=lambda  x: fail[x], reverse=True)
