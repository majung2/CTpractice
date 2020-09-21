# 정확성만 통과

import re
def solution(info, query):
    answer = []
    split_score_com = re.compile('([a-z -]+) (\d+)') # 문자부분과 숫자부분으로 분리

    for i in range(len(info)):
        temp = split_score_com.findall(info[i])
        info[i] = [temp[0][0],int(temp[0][1])]
    for i in range(len(query)):
        temp = split_score_com.findall(query[i])
        q, s = temp[0][0], int(temp[0][1])
        q = re.sub('[-]','[a-z]+',q)
        q = re.sub(' and ',') (',q)
        q = '('+q+')'
        query[i] = [q,s]

    for q, s in query:
        x = re.compile(q)
        count = 0
        for i in info:
            content, score = i[0], i[1]
            if x.match(content) and score >= s:
                count += 1
        answer.append(count)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)

