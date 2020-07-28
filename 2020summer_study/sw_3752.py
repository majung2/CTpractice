# 가능한 시험 점수
# 통과!

T = int(input()) # 테스트 케이스 수

for i in range(T):
    N = int(input()) # 문제 수
    points = list(map(int,input().split())) # 문제별 배점
    scores = {0}

    for point in points:
        temp = []
        for score in scores:
            temp.append(score+point)
        scores.update(temp)

    
    score = len(scores)

    answer = f'#{i+1} {score}'
    print(answer)
