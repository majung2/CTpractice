# 히스토그램
# 시간초과
from collections import deque

N = int(input())
his = []

for _ in range(N):
    his.append(int(input()))

maxA = 0

for i in range(N):
    
    s, e = 0,i # 밑변 시작, 끝 점

    # 시작 인덱스 찾기
    if i !=0 and his[i] > his[i-1]: # 이전보다 큼
        s = i # 현재인덱스에서 시작
    else: # 이전보다 같거나 작음
        for j in range(i-1,0,-1): 
            if his[j] >= his[i]:
                continue
            else:
                s = j+1
                break

    # 끝점찾기
    for j in range(i,N):
        if his[j] < his[i]:
            break
        e = j
    
    maxA = max(maxA,his[i]*(e-s+1))


print(maxA)