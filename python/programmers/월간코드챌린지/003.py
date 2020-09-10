import sys
sys.setrecursionlimit(2000)

result = set()
def dfs(a,i,flag):
    if len(a) == 1: 
        result.add(a[0])
        return
    # 오른쪽
    if i+1 < len(a):
        dfs(a[:i] + [min(a[i],a[i+1])] + a[i+2:], i, flag)
    # 왼쪽
    if i-1 >= 0:
        dfs(a[:i-1] + [min(a[i-1], a[i])] + a[i+1:], i-1, flag)
        
    if not flag: # 안 터트림
        if i+1 < len(a):
            dfs(a[:i] + [max(a[i],a[i+1])] + a[i+2:], i, True)
        # 왼쪽
        if i-1 >= 0:
            dfs(a[:i-1] + [max(a[i-1], a[i])] + a[i+1:], i-1, True)
            
    
    

def solution(a):
    idx = a.index(min(a))
    dfs(a,idx,False)
    answer = len(result)
    print(result)
    
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))