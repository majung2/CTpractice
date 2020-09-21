def solution(boxes):
    answer = len(boxes)
    stock = []
    
    for x, y in boxes:
        if x in stock:
            stock.remove(x)
            answer -= 1
        else:
            stock.append(x)
        if y in stock:
            stock.remove(y)
            answer -= 1
        else:
            stock.append(y)
            
    
    return answer