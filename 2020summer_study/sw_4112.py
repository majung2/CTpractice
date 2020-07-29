# 이상한 피라미드 탐험

T = int(input()) # 테스트케이스 수

def NM(num):
    N = 1 # N 번째 줄
    while(num-N>0): 
        num -= N
        N += 1
    # num == M 번째 수
    return ([N,num])

for test_case in range(1,T+1):
    a, b = map(int, input().split())
    answer = 0
    if a != b: # 같으면 할 필요없이 0
        sm = b if a > b else a
        bg = a if a > b else b

        lst = []
        lst.append(NM(sm)) # 작은 수의 위치정보
        lst.append(NM(bg)) # 큰 수의 위치정보

        if lst[0][1] < lst[1][1]: # 작은 수의 M < 큰 수의 M 인 경우 : 오른쪽으로 내려가기
            absN = abs(lst[0][0]-lst[1][0]) # N끼리의 차 와
            absM = abs(lst[0][1]-lst[1][1]) # M끼리의 차 중
            answer += absN if absN > absM else absM # 큰 값이 답
        else: # 왼쪽으로 내려감
            answer += (lst[1][0]-lst[0][0]) # 작은 수 N 이 큰 수 N과 같아질때까지 내려가고
            answer += (lst[0][1]-lst[1][1]) # 작은 수, 큰 수의 M 차이만큼 answer 증가

    print(f'#{test_case} {answer}')