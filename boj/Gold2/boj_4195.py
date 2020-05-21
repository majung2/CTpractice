# 친구 네트워크
# 중
# 해시, 집합, 그래프
# 못품 / 50분

# 인강 풀이

# 해시를 활용한 Union-Find 알고리즘
# Python은 dictionay로 해시 활용 가능


def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]


def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
        print(number[find(x)])





    
        










                
            
            
                
                
