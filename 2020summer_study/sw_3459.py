# 승자 예측하기
# 실패

# T 테스트케이스 수
T = int(input())
player = ['Alice','Bob']

def change():
    global winner
    if winner == 1:
        winner = 0
    else:
        winner = 1

for test_case in range(1, T + 1):
    N = int(input())
    winner = 0
    result = 1

    while result <= N:
        if result*2<=N or result*2+1<=N:
            result*=2
        change()
        

    answer = f'#{test_case} {player[winner]}'
    print(answer)

    
