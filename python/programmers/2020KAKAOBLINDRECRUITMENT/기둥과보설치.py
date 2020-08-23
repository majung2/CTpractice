n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# 주어지는 입력

def solution(n, build_frame):
    answer = [[]]
    wall = [0 for _ in range(n+1)]

    for x,y,a,b in build_frame: # a 0기둥 1보, b 0삭제 1설치
        if b == 0: # 삭제
            




        elif b == 1: # 설치





    return answer




# 결과 출력
print(solution(n,build_frame))