# 숨바꼭질 2
import math

N, K = map(int, input().split()) # 수빈, 동생 위치

way = {}
cur_min = math.ceil(math.log2(K-N)+1)

def dfs(n, k, t):
    global cur_min
    if n == k: # 찾음
        if t <= cur_min:
            if t in way:
                way[t] += 1
            else:
                way[t] = 1
            cur_min = min(cur_min, t)
        return
    elif n < 0 or n > 100000:
        return
    elif cur_min < t:
        return
    else:
        if n != 0:
            dfs(n*2, k, t+1)
        dfs(n+1, k, t+1)
        dfs(n-1, k, t+1)

dfs(N, K, 0)

s_way = sorted(way.items())

print(s_way[0][0])
print(s_way[0][1])