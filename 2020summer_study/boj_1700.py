# 멀티탭 스케줄링
# 통과

# N 멀티탭 구멍의 개수
# K 전기용품 사용 횟수
# 전기용품 이름 K 이하 자연수로

N, K = map(int,input().split())
plugs = list(map(int, input().split()))

tap = [0 for _ in range(N)] # 현재 멀티탭에 꽂혀있는 플러그 정보

count = {}

answer = 0 # 플러그 빼는 최적의 횟수

def findMin(tap): # 가장 가까운 같은 plug까지의 거리가 가장 먼 것 찾기
    global plugs
    cPlug = tap[0]
    for data in tap:
        if data not in plugs: # 앞으로 안 씀
            cPlug = data
            break
        else:
            if plugs.index(cPlug)<plugs.index(data):
                cPlug = data
    return tap.index(cPlug)

for data in plugs:
    if data not in tap: # 이미 꽂혀있지 않음
        if 0 in tap: # 빈 구멍이 있음
            tap[tap.index(0)]=data
        else: # 하나 빼야하는 경우!!
            tap[findMin(tap)] = data
            answer +=1
    plugs[plugs.index(data)]=0 # 이미 사용한 것 0으로 바꾸기
    
print(answer)
            








