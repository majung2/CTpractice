def solution(ball, order):
    answer = []
    while(ball):
        if order.index(ball[0]) > order.index(ball[-1]): # 오른쪽 끝 빼기
            answer.append(ball.pop())
        else:
            answer.append(ball.pop(0))
    
    return answer