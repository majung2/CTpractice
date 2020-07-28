# 사다리조작
# 브루트포스

# N 세로선의 수
# H 가로선을 놓을 수 잇는 위치
# M 가로선의 수

# 첫째줄 입력 N, M, H
# 둘째줄부터 가로선의 정보 a, b 
# a 위치에 b - b+1 연결하는 선

N, M, H = map(int, input().split())
lines = []
count = [0 for i in range(N)]
answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    lines.append((a,b))
    count[b] += 1


for i in range(1,N):
    if count[i]%2 == 0: # 짝수개 연결되어 있으면 패스
        continue
    else: # 홀수개 연결되어 있으면 연속 선 아닌 것으로 추가!
        check = answer
        for h in range(1,H+1):
            if (h,i-1) in lines or (h,i) in lines or (h,i+1) in lines:
                continue
            else:
                lines.append((h,i))
                answer += 1
                break
        if check == answer:
            answer = -1
            break

        
if answer > 3:
    answer = -1

print(answer)

            
        


