# 이름궁합 테스트

N, M = map(int, input().split())
A, B = input().split()

alpha_count = {'A':3, 'B':2, 'C':1, 'D':2, 'E':4, 'F':3, 'G':1, 'H':3, 'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':2, 'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1, 'V':1, 'W':1, 'X':2, 'Y':2, 'Z':1}

list =[]

for i in range(max(N,M)):
    if i<N:
        list.append(alpha_count[A[i]])
    if i<M:
        list.append(alpha_count[B[i]])

while len(list)>2:
    for i in range((len(list)-1)):
        if i<len(list)-1:
            list[i] = (list[i]+list[i+1])%10
    list.pop()

answer = list[0]*10 + list[1]

print("%d%%" % answer)

# 다른 풀이 (알고리즘 인강ver)
'''
N, M = map(int, input().split())
A, B = input().split()

alp = [3,2,1,2,4,3,1,3,1,1,3,1,3,2,1,2,2,2,1,2,1,1,1,2,2,1]

AB = ''
min_len = min(N,M)

for i in range(min_len):
    AB += A[i]+B[i]

AB += A[min_len:] + B[min_len:]

lst = [alp[ord(i)-ord('A')] for i in AB]

for i in range(N+M-2):
    for j in range(N+M-1-i):
        lst[j] += lst[j+1]

print("{}%".format(lst[0] % 10*10 + lst[1] % 10))

'''