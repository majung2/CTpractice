def solution(k, score):
    answer = -1
    N = len(score) # 총 점수 갯수
    sub = [0 for _ in range(N)]
    sub_count = {}
    remove = [False for _ in range(N)] # False: 조작x True: 조작o

    for i in range(1,N):
        sub[i] = score[i-1] - score[i]
        if sub[i] not in sub_count:
            sub_count[sub[i]] = 1
        else:
            sub_count[sub[i]] += 1

    for i in range(1,N):
        if sub_count[sub[i]] >= k:
            remove[i-1], remove[i] = True, True

    answer = remove.count(False)

    return answer