# APC는 왜 서브태스크 대회가 되었을까?
# 46분
# Bronze 2

N, L, K = map(int, input().split()) # 문제의 개수, 현정이의 역량, 풀수 있는 최대 문제 수
task, sub_task = [],[] # 문제 난이도 (sub1, sub2)
score = 0

for i in range(N):
    task.append(tuple(map(int, input().split())))

for sub in task:
    if K and sub[1] <= L:
        score+=140
        K -= 1
    else:
        sub_task.append(sub)

for sub in sub_task:
    if K and sub[0] <= L:
        score+=100
        K-=1

print(score)

# 인강풀이
# N, L, K = map(int, input().split()) 

# easy, hard = 0,0 # easy는 쉬운 문제 '만' 풀수 있는 것

# for i in range(N):
#     sub1, sub2 = map(int, input().split())
#     if sub2 <= L:
#         hard += 1
#     elif sub1 <= L:
#         easy += 1

# # hard 문제
# ans = min(hard,K) * 140

# # esay 문제
# if hard < K:
#     ans+= min(K-hard, easy) * 100

# print(ans)

