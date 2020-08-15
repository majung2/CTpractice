# 백업
# 틀렸습니다

n, k = map(int, input().split()) # 회사 수, 케이블 수
company = [0 for _ in range(n)]
dis = [0 for _ in range(n-1)] # 거리만

for i in range(n):
    company[i] = int(input())

for i in range(n-1):
    dis[i] = company[i+1]-company[i]


A, B = [],[] # 좌표 인덱스 담는 배열
Aidx, Bidx = -2,-2
for i in range(n-1):
    if Aidx + 1 < i: # 연속인지 확인
        if len(A) != k: # A 배열이 다 안찼으면 바로 넣기
            A.append(dis[i])
            Aidx = i
            continue
        elif max(A) > dis[i]: # 다 찼으면 가장 큰값과 비교
            A.remove(max(A)) 
            A.append(dis[i])
            Aidx = i
            continue
    if Bidx + 1 < i:
        if len(B) != k:
            B.append(dis[i])
            Bidx = i
            continue
        elif max(B) > dis[i]:
            B.remove(max(B))
            B.append(dis[i])
            Bidx = i
            continue

if len(A) == k and len(B) == k:
    print(min(sum(A),sum(B)))
elif len(A) == k:
    print(sum(A))
elif len(B) == k:
    print(sum(B))

