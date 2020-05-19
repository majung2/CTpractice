# 나이순 정렬
# 하
# 정렬
# 18 / 15분

N = int(input())
result = []

for _ in range(N):
    age, name = map(str, input().split())
    age=int(age)
    result.append((age,name))

print(result)
result = sorted(result, key=lambda person: person[0])
print(result)

for i in result:
    print(i[0],i[1])


# 인강 풀이
# n = int(input())
# array = []

# for _ in range(n):
#     input_data = input().split()
#     array.append((int(input_data[0]),input_data[1]))

# array = sorted(array, key=lambda x:x[0])

# for i in array:
#     print(i[0],i[1])
    
        
