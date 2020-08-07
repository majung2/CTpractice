# 연속합

n = int(input())
numbers = list(map(int, input().split()))
max = -1000
min = 1000
sum = 0

for num in numbers:
    sum += num
    if sum <= min:
        min = sum

    if num > max: # 반례 -4 -3 -2 -1 -10
        max =num    
    if sum >= max:
        max = sum
    if sum!=min and sum-min > max:
        max = sum-min
print(max)

    



