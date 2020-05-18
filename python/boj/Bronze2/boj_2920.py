# 음계
# 10분(걸린시간) / 15분(권장시간)

N = list(map(int,input().split(' ')))

def check(N):
    if N[0]==1:
        num = 1
        for i in N:
            if i == num:
                num+=1
            else:
                return 'mixed'
        if num == 9:
            return 'ascending'
    elif N[0] == 8:
        num = 8
        for i in N:
            if i == num:
                num -= 1
            else:
                return 'mixed'
        if num == 0:
            return 'descending'
    else:
        return 'mixed'

print(check(N))

# 인강풀이
# a = list(map(int, input().split(' ')))

# ascending = True
# descending = True

# for i in range(1,8):
#     if a[i]>a[i-1]:
#         descending = False
#     elif a[i]<a[i-1]:
#         ascending = False

# if ascending:
#     print('ascending')
# elif descending:
#     print('descending')
# else:
#     print('mixed')