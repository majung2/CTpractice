# 알쏭달쏭 정렬

lst = list(map(str,input().split()))
order = ['8','5','2','4','3','7','6','1','0','9']

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if order.index(lst[j]) > order.index(lst[j+1]):
            lst[j],lst[j+1] = lst[j+1],lst[j]
print(' '.join(lst))
