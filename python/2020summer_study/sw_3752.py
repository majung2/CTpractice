# 가능한 시험 점수
# 통과!
T = int(input()) # 테스트 케이스 수

for i in range(T):
    N = int(input()) # 문제 수
    points = list(map(int,input().split())) # 문제별 배점
    scores = {0}

    for point in points: # 점수 하나씩 보기
        temp = [] # 임시 리스트
        for score in scores: # 이미 score에 있는 점수에 point 더해서 넣기
            temp.append(score+point)
        scores.update(temp)

    
    score = len(scores) # 집합의 길이 구하기 (중복제거)

    answer = f'#{i+1} {score}'
    print(answer)