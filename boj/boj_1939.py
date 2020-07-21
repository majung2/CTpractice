# 중량제한

# 인강풀이
from collections import deque

n, m = map(int, input().split()) # n: 섬, m: 다리
adj = [[] for _ in range(n+1)]

# c 무게로 갈 수 있는 경로 있는 지 확인
def bfs(c): 
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True

    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    
    return visited[end_node]


start = 100000000
end = 1

for _ in range(m):
    x, y, w = map(int, input().split())
    adj[x].append((y,w))
    adj[y].append((x,w))
    start = min(start, w)
    end = max(end, w)

start_node, end_node = map(int, input().split())

result = start
while (start<=end):
    mid = (start + end)//2
    if (bfs(mid)):
        result = mid
        start = mid+1
    else:
        end = mid-1

print(result)