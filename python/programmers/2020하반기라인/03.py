def find(c, n):
    if n < 10:
        return c, n
    else:
        s = str(n)
        count, num = 50, 0
        temp_c, temp_n = 50, 0 
        for i in range(len(s)-1):
            front, back = s[:i+1], s[i+1:]
            if back[0] == '0':
                continue
            else:
                temp_c, temp_n = find(c+1, int(front)+int(back))
                if count > temp_c:
                    count, num = temp_c, temp_n
        return count, num
            
def solution(n):    
    a, b = find(0,n)
    answer = [a,b]

    return answer