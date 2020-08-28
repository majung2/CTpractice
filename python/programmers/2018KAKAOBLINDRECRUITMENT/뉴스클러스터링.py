import math
def solution(str1, str2):
    answer = 0
 
    str1, str2 = str1.upper(), str2.upper() # 대문자로 모두 변환 아스키 65이상 90이하
    l1, l2 = len(str1), len(str2)
    A, B = [],[] # 다중집합
    inter, union = [],[] # 교집합 , 합집합


    for i in range(l1-1):
        temp1,temp2 = str1[i],str1[i+1]
        if ord(temp1) < 65 or ord(temp1) > 90: #다른 문자or숫자
            continue
        elif ord(temp2) < 65 or ord(temp2) > 90: 
            continue
        else:
            A.append(temp1+temp2)
    union += A
    
    for i in range(l2-1):
        temp1, temp2 = str2[i], str2[i+1]
        if ord(temp1) < 65 or ord(temp1) > 90: #다른 문자or숫자
            continue
        elif ord(temp2) < 65 or ord(temp2) > 90: 
            continue
        else:
            temp = temp1+temp2
            B.append(temp)
            if temp in A: 
                inter.append(temp)
                A.remove(temp)
            else:
                union.append(temp)

    if len(union)==0:
        ja = 1
    else:
        ja = len(inter)/len(union)

    answer = math.floor(ja*65536)
    return answer
