from sys import *
setrecursionlimit(10**4)
# 위 코드 추가해서 통과!!!


def dfs(j_type, x, y, v, check, n):
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    if check[x][y]:
        return
    else:
        check[x][y] = 1

        for i in range(4):
            xx, yy = x + dx[i], y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= n:
                continue
            elif v[xx][yy] != j_type:
                continue
            else:
                dfs(j_type, xx, yy, v, check, n)
        return
    
    

def solution(v):
    n = len(v)
    answer = [0 for _ in range(3)]
    check = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not check[i][j]:
                jak = v[i][j]
                dfs(v[i][j], i, j, v, check, n)
                answer[jak] += 1
                
    return answer

print(solution([[0,0,1,1],[1,1,1,1],[2,2,2,1],[0,0,0,2]]))
# print(solution([[0,0,1],[2,2,1],[0,0,0]]))
