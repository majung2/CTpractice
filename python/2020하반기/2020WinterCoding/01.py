def solution(n, delivery):
    answer = ''
    result = ['?' for _ in range(n)] # index = 상품번호-1
    
    # 재고 있는 것부터 확인
    for a, b, d in delivery:
        if d:
            result[a-1] = 'O'
            result[b-1] = 'O'
    
    for a, b, d in delivery:
        if not d:
            if result[a-1] == 'O':
                result[b-1] = 'X'
            elif result[b-1] == 'O':
                result[a-1] = 'X'
    
    answer = ''.join(result)

    
    return answer