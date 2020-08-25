# 수영장

T = int(input())
ticket = [0 for _ in range(4)] # 이용권 금액
mon_use = [0 for _ in range(12)] # 월별 이용일 -> 이용금액


def three_check(start, end):
    global ticket, mon_use
    if start>end:
        return 0
    elif end-start<3:
        return min(sum(mon_use[start:end+1]),ticket[2])
    else:
        total = ticket[3]
        for i in range(3):
            temp = sum(mon_use[start:start+i])
            temp_end = min(end,start+i+2)
            temp += (three_check(start+i,temp_end) + three_check(start+i+3,end))
            total = min(temp,total)
        return total

for test_case in range(1,T+1):
    ticket = list(map(int, input().split()))
    mon_use = list(map(int, input().split()))
    price = 0
    d_count = 0 # 한달 이용권이 싸게되는 날짜
    start, end = -1, -1

    while(ticket[0]*d_count < ticket[1]):
        d_count+=1

    for i in range(12): # 일, 월 비교
        if mon_use[i] > 0 and start == -1:
            start = i
        if mon_use[i] > 0:
            end = i
        if mon_use[i] < d_count: # 일 이용권이 유리
            mon_use[i]*=ticket[0]
        else:
            mon_use[i] = ticket[1]
    price = sum(mon_use)

    # 세달
    price = min(price, three_check(start, end))


    # 일년
    price = min(price, ticket[3])
    print(f"#{test_case} {price}")