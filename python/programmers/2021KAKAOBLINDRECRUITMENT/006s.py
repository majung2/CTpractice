import copy
dx, dy = [-1,0,1,0],[0,1,0,-1]
count = 100
B = []
loc = []

def dfs(x, y, t, c, l): #좌표, 종류, 체크, 길이
    global count, B, loc
    current_c = copy.deepcopy(c)

    if B[x][y] == t:
        count = min(count, l)
        loc = [x,y]
        return

    else:
        current_c[x][y] = 1
        for i in range(4):
            xx, yy = x, y
            while(True):
                if xx+dx[i] < 0 or xx+dx[i]>3 or yy+dy[i] < 0 or yy+dy[i]>3: # 벽 만남
                    break
                else: # 벽이 아니면 움직임
                    xx+=dx[i]
                    yy+=dy[i]
                    if B[xx][yy]: # 카드만남
                        break
                    current_c[xx][yy] = 1

            if not current_c[xx][yy]:
                dfs(xx, yy, t, current_c, l+1)

def solution(board, r, c):
    global count, B, loc
    B = board
    answer = 0
    c_type = B[r][c]
    
    while(True):
        # 짝궁찾기
        if c_type:
            count, B[r][c] = 100, 0 # 초기화
            check = [[0 for _ in range(4)] for _ in range(4)]
            dfs(r, c, c_type, check, 1)
            r, c = loc[0],loc[1]
            answer += count

            B[r][c] = 0
            c_type = 0
        
        else:
            count = 1
            q = [[r,c]]
            check = [[0 for _ in range(4)] for _ in range(4)]
            while(q):
                temp = q.pop()
                x, y = temp[0], temp[1]
                for i in range(4):
                    xx, yy = x, y
                    while(True):
                        if xx+dx[i] < 0 or xx+dx[i]>3 or yy+dy[i] < 0 or yy+dy[i]>3: # 벽 만남
                            break
                        else: # 벽이 아니면 움직임
                            xx+=dx[i]
                            yy+=dy[i]
                            check[xx][yy] = 1
                            if B[xx][yy]: # 카드만남
                                break
                    if B[xx][yy]:
                        c_type = B[xx][yy]
                        r, c = xx, yy
                        q = []
                        break
                    else:
                        if not check[xx][yy]:
                            q.append([xx,yy])
                count += 1
            if B[r][c] == 0: # 더이상 할 것이 없음
                break
            else:
                answer += count
            
        print(answer)

    
    return answer


solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)