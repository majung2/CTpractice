# 수 정렬하기 3
# 하
# 정렬
# 20분
# Silver 4

# 메모리초과

# 인강 풀이
# 시간복잡도 O(N)의 정렬 알고리즘 이용

import sys

n = int(sys.stdin.readline())
array = [0]*10001

for i in range(n):
    data = int(sys.stdin.readline())
    array[data]+=1

for i in range(10001):
    if array[i]!=0:
        for j in range(array[i]):
            print(i)