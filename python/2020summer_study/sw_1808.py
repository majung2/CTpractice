# 지희의 고장난 계산기

T = int(input())
cal = [] # index가 숫자
num, answer = 0, 1

def contain(number): # 각 자리수 모두 누를 수 있으면 자리수 반환 없으면 0
    global cal
    count = 0
    while(number):
        if cal[number%10]:
            count += 1
            number//=10
        else:
            count = 0
            break
    return count


for test_case in range(1,T+1):
    cal = list(map(int, input().split()))
    num = int(input())

    while(num):
        temp = contain(num)
        if temp:
            answer += temp
            num = 0
        else:
                            





    print(f"#{test_case} {answer}")