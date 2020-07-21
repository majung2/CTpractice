# 스택 수열
# 스택, 그리기
# 19 / 30분
# Silver 3

n = int(input())
data=[]
for i in range(n):
    data.append(int(input()))

stack = []
loc = 0
result=[]
for i in range(1,n+1):
    if i <= data[loc]:
        stack.append(i)
        result.append("+")
    while len(stack) and stack[-1] == data[loc]:
        stack.pop()
        result.append("-")
        loc +=1

if len(stack):
    print("NO")
else:
    for i in result:
        print(i)


# 인강풀이

# n = int(input())
# count = 1
# stack = []
# result =[]

# for i in range(1,n+1):
#     data = int(input())
#     while count <= data:
#         stack.append(count)
#         count+=1
#         result.append('+')
#     if stack[-1]==data:
#         stack.pop()
#         result.append('-')
#     else:
#         print('NO')
#         exit(0)
# print('\n'.join(result))



