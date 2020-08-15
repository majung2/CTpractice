key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1, 1], [1, 1, 0, 1], [1, 0, 1, 1], [1,0,1,1]]

######
key_attr = [] # key 후보 (key회전해서 나온 것들)

def smallpart(lst):
    minX, minY = 20,20
    for x,y in lst:
        minX, minY = min(minX,x), min(minY,y)
    for i in lst:
        i[0] -= minX
        i[1] -= minY
    sizeX, sizeY = 0,0
    for x,y in lst:
        sizeX, sizeY = max(sizeX, x), max(sizeY,y)
    return lst, sizeX,sizeY
    
def keyAttr(lst, n, m):
    global key_attr
    key_attr.append(lst)

    temp = []
    # 90도 회전
    for x,y in lst:
        xx = y
        yy = n-x
        temp.append([xx,yy])
    key_attr.append(temp)

    lst,temp = temp, []
    # 180도 회전
    for x,y in lst:
        xx = y
        yy = m-x
        temp.append([xx,yy])
    key_attr.append(temp)

    lst, temp = temp, []
    # 270도 회전
    for x, y in lst:
        xx = y
        yy = n-x
        temp.append([xx,yy])
    key_attr.append(temp)

def solution(key, lock):
    answer = True
    N, M = len(lock), len(key)
    lock_hom, key_dol = [], []

    # lock 홈 위치/갯수 파악
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_hom.append([i,j])
    # key 돌기 위치/갯수 파악
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                key_dol.append([i,j])

    # lock의 홈 갯수 > key의 돌기 갯수
    if len(lock_hom) > len(key_dol): 
        return False

    # 갯수 같은 경우
    elif len(lock_hom) == len(key_dol):
        key_dol, kx, ky = smallpart(key_dol) 
        lock_hom, _, _ = smallpart(lock_hom)
        keyAttr(key_dol, kx, ky)
        if lock_hom in key_attr:
            return True
        else:
            return False
    
    # lock의 홈 갯수 < key 돌기 갯수
    else:
        key_dol, kx, ky = smallpart(key_dol) 
        lock_hom, _, _ = smallpart(lock_hom)

    return answer

print(solution(key, lock))