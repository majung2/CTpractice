# 20분
def turnIntoMap(n, arr):
    Map = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        temp = arr[i]
        for j in range(n-1,-1,-1):
            Map[i][j] = temp%2
            temp//=2
    
    return Map

def solution(n, arr1, arr2):
    answer = [0 for _ in range(n)]
    map1, map2 = turnIntoMap(n,arr1), turnIntoMap(n, arr2)

    for i in range(n):
        temp = ''
        for j in range(n):
            if max(map1[i][j], map2[i][j]) == 1:
                temp += '#'
            else:
                temp += ' '
        answer[i] = temp
    return answer