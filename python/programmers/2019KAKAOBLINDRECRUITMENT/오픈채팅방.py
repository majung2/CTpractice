# 25분
def solution(record):
    answer, record_t = [],[]
    nickname = {}
    nick_record = []

    for i in range(len(record)):
        record_t.append(record[i].split())
    
    for r in record_t:
        if len(r)>2: # Enter or Change
            nickname[r[1]] = r[2]
            if r[0] == 'Enter':
                nick_record.append([r[1], 1])
        else:
            nick_record.append([r[1], 0])

    for userId, status in nick_record:
        if status:
            answer.append(nickname[userId]+"님이 들어왔습니다.")
        else:
            answer.append(nickname[userId]+"님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))