# 짚신벌레
# 시간초과

# a 성체가 되는 날 = 새로운 개체 생성
# b 새로운 개체 만들지 않는날
# d 죽는날
# N 일째

a, b, d, N = map(int, input().split())
tank = [0] # 짚신벌레 담긴 수조

for _ in range(N):
    count = 0
    for bug in tank:
        tank[tank.index(bug)]= bug+1
        if bug+1 >= a and bug+1 < b:
            count +=1
    if tank[0]==d:
        del tank[0]
    for _ in range(count):
        tank.append(0)

answer = len(tank)%1000
print(answer)
