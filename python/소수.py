import time, math

N = 4000000

T = time.time()
decimal = [] 


# 후보1
for i in range(2,N+1):
    flag = True
    for j in range(2, math.floor(i ** 0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        decimal.append(i)

# 후보2
# check = [0,0] + [1 for _ in range(N-1)]
# for p in range(2, N+1):
#     if check[p] == 0:
#         continue
#     else:
#         decimal.append(p)
#         for i in range(2 * p, N+1, p):
#             check[i] = 0



print("time:", time.time()-T)