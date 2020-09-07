# 1시간...
pre = 0

def cal(p, s, b, o):
    global pre
    sub_cal = 0
    if b == 'X':
        return 0
    else:
        if b == 'S':
            sub_cal = s
        elif b == 'D':
            sub_cal = s*s
        elif b == 'T':
            sub_cal = s*s*s
        if o == '*':
            sub_cal, pre = (sub_cal*2+pre), sub_cal*2
            return sub_cal
        elif o == '#':
            pre = sub_cal * -1
            return sub_cal*-1
        else:
            pre = sub_cal
            return sub_cal

def solution(dartResult):
    answer = 0
    R_list = list(dartResult)
    num = ['0','1','2','3','4','5','6','7','8','9']
    global pre
    bonus = 'X' # 초기화
    option = 0
    current = -1
    flag = False

    for i in range(len(R_list)+1):
        if i == len(R_list):
            answer += cal(pre, current, bonus, option)
            break
        elif flag == False and R_list[i] in num:
            answer += cal(pre, current, bonus, option)
            option = 0
        if R_list[i] in num:
            if flag: # 10인 경우
                current*=10
                flag = False
            else:
                current = int(R_list[i])
                flag = True
        elif R_list[i] in ['S','D','T']:
            bonus = R_list[i]
            flag = False
        else:
            option = R_list[i]
            flag = False
    return answer

print(solution('1D2S#10S'))