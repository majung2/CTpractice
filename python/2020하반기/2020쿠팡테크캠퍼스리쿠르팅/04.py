N, R = 0, []
def count_road(start, end, c): # start 부터 end 까지 경로 수 구하는 함수
    c_check = c[:]
    c_check[start], c_check[end] = 1, 1
    count = 0

    if R[start][end]:
        count +=1

    if R[start].count(1):
        for m in range(N):
            if start == m or end == m:
                continue
            if c_check[m]:
                continue
            if R[start][m] and R[m][end]:
                count += count_road(start, m, c_check) * count_road(m, end, c_check)                

    return count

def solution(depar, hub, dest, roads):
    global N, R
    N = len(roads)*2
    R = [[0 for _ in range(N)] for _ in range(N)] # 도로정보 2차원 배열

    city_num = {}
    count = 0
    for start, end in roads:
        if start not in city_num:
            city_num[start] = count
            count += 1
        if end not in city_num:
            city_num[end] = count
            count += 1
        R[city_num[start]][city_num[end]] = 1
    N = count
    check = [0 for _ in range(N)] # 0 안 간곳, 1 간 곳
    for i in range(N):
        R[i] = R[i][:N]
    R = R[:N]


    a, b =count_road(city_num[depar], city_num[hub], check[:]) ,count_road(city_num[hub], city_num[dest], check[:]) 
    if a:
        a -= 1
    if b:
        b -= 1
    answer = a * b 
    return answer