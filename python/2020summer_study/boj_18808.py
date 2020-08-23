# 스티커 붙이기

N, M, K = map(int, input().split()) # 노트북 세로, 가로, 스티커 개수

notebook = [[0 for _ in range(N)] for _ in range(M)]
stickers = [0 for _ in range(K)] # 모든 스티커 정보 담는 3차원 배열
sticker_rc = [0 for _ in range(K)]

for i in range(K):
    r, c = map(int, input().split())
    stickers_rc[i] = [r,c]
    st = [0 for _ in range(r)]
    for j in range(r):
        st[j] = list(map(int, input().split()))
    stickers[i] = st[:]

# 붙일 수 있는지 확인 후 가능하면 붙이기
def check(k,si,sj): # 스티커번호, notebook에서 비교 시작 위치
    global sticker_rc, notebook, stickers
    r, c = sticker_rc[k][0],sticker_rc[k][1]
    for i in range(r):
        for j in range(c):
            if notebook[si+i][sj+j]+stickers[k][i][j] == 2:
                return False
    for i in range(r):
        for j in range(c):
            notebook[si+i][sj+j] = stickers_rc[k][i][j]
    return True

def search(k):
    global sticker_rc
    r, c = sticker_rc[k][0],sticker_rc[k][1]
    for i in range(N-r+1):
        for j in range(M-c+1):
            if check(i,j):
                return True
            else:
                return False

def rotate(k):


for k in range(K): # 스티커 인덱스
    for _ in range(4):
        if search(k):
            break
        else:
            idx = rotate(k) # 스티커 회전 후 stickers의 마지막에 추가 후 인덱스 반환
            search(idx)


answer = 0
for i in range(N):
    for j in range(M):
        if notebook[i][j] != 0:
            answer += 1

print(answer)

