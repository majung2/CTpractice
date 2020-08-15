n, weak, dist = 12, [1,5,6,10], [1,2,3,4]
# n, weak, dist = 12, [1,3,4,9,10], [3,5,7]

#####
next_dis = [0 for _ in range(len(weak))]


def check(dis, weak, n):
    global next_dis
    for i in weak:
        

def solution(n, weak, dist):
    answer = 0
    dist = dist.sort(reverse=True)
    global next_dis

    for i in range(len(weak)-1):
        next_dis[i] = weak[i+1]-weak[i]
    next_dis[-1] = n - weak[-1] + weak[0]



    cur_dis = dist.pop(0)



    



    return answer

print(solution(n, weak, dist))