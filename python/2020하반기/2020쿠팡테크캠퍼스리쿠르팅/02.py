import datetime

def solution(n, customers):
    answer = 0
    e_time = [datetime.datetime(2020,1,1,0,0,0) for _ in range(n)] # 업무 완료시간
    key_c = [0 for _ in range(n)] # 키오스크 별 사용 횟수

    match_key = 0
    for custom_info in customers:
        a_date, a_time, s_time = map(str, custom_info.split())
        mon, day = map(int, a_date.split('/'))
        hour, minute, second = map(int, a_time.split(':'))
        s_time = int(s_time)

        c_datetime = datetime.datetime(2020,mon,day,hour,minute,second)

        match_key = e_time.index(min(e_time)) # 가장 일찍 끝나는 키오스크 선택
        key_c[match_key] += 1
        if min(e_time) < c_datetime: # 현재 운영되지 않는 키오스크 존재
            e_time[match_key] = c_datetime + datetime.timedelta(minutes=s_time) # 손님 도착 시간부터 업무 수행
        else: # 모든 키오스크 운영중
            e_time[match_key] += datetime.timedelta(minutes=s_time) # 운영 종료 후 업무 수행

    answer = max(key_c)

    return answer