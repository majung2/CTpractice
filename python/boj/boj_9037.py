# The candy war
# Silver 5
# 42분

T = int(input()) #test case 수

def cir(li): # 순환시키기
    new = []
    if len(li)>1:
        for i in range(len(li)):
            new.append(li[i]//2 + li[i-1]//2)
    else:
        return li
    return new


def make_even(li): # 짝수로 만들기
    new = []
    for i in li:
        if i%2 == 0:
            new.append(i)
        else:
            new.append(i+1)
    return new

def check(li): # 모두 같은지 확인 
    for i in range(len(li)-1):
        if li[i]!=li[i+1]:
            return False
    return True

for _ in range(T):
    N = int(input()) # 아이의 수
    C = list(map(int, input().split())) # 초기 사탕 수
    count = 0 # 순환 수

    C = make_even(C)
    while not check(C):
        C = cir(C)
        C = make_even(C)
        count+=1
    
    print(count)



# 인강풀이

# def check(N, candy):
#     for i in range(N):
#         if candy[i] % 2 == 1:
#             candy[i]+=1
#     return len(set(candy)) == 1 # 배열의 수가 모두 같은지 확인!

# def teacher(N, candy):
#     tmp_lst = [0 for i in range(N)]
#     for idx in range(N):
#         if candy[idx] % 2:
#             candy[idx] += 1
#         candy[idx] //= 2
#         tmp_lst[(idx+1) % N] = candy[idx]
    
#     for idx in range(N):
#         candy[idx] += tmp_lst[idx]
    
#     return candy

# def process():
#     N, candy = int(input()), list(map(int, input().split()))
#     cnt = 0
#     while not check(N, candy):
#         cnt += 1
#         candy = teacher(N, candy)
#     print(cnt)

# for i in range(int(input())):
#     process()





