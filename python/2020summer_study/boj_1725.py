N = int(input())
his = []

for _ in range(N):
    his.append(int(input()))

areas = set() # 넓이 집합
index = {}

for i in range(N):
    s, e = 0,i # 밑변 시작, 끝 점

    # 시작 인덱스 찾기
    if i !=0 and his[i] > his[i-1]: # 이전보다 큼
        s = i # 현재인덱스에서 시작
    else: # 이전보다 같거나 작음
        for j in range(i): 
            if his[j] < his[i]:
                s = j+1

    # 끝점찾기
    for j in range(i,N):
        if his[j] < his[i]:
            break
        e = j
    
    areas.add(his[i]*(e-s+1))
    
print(max(areas))