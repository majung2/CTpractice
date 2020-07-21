# Mixing Milk
# 1시간
# Bronze 2

c1, m1 = map(int, input().split())
c2, m2 = map(int, input().split())
c3, m3 = map(int, input().split())

milk = {0:(0,0,0)}
count = 1
first = 0

def move(m1,m2,m3):
    global count, first
    if (m1,m2,m3) not in milk.values():
        milk[count]=(m1,m2,m3)
        count+=1
        return 0
    else:
        for key, value in milk.items():
            if value == (m1,m2,m3):
                first = key
                return first


while True:
    # c1 -> c2
    temp = m2
    m2 = min(c2, m1+m2)
    m1 -= m2-temp
    if move(m1,m2,m3):
        break

    # c2 -> c3
    temp = m3
    m3 = min(c3, m2+m3)
    m2 -= m3-temp
    if move(m1,m2,m3):
        break
    
    # c3 -> c1
    temp = m1
    m1 = min(c1, m1+m3)
    m3 -= m1-temp
    if move(m1,m2,m3):
        break

div = (101-first)%(count-first)
if div == 0:
    result = milk[count-1]
else:
    result = milk[first+div-1]

for i in result:
    print(i)



    

# 인강 풀이
C, M = [0,0,0], [0,0,0]

for i in range(3):
    C[i], M[i] = map(int, input().split())

for i in range(100):
    idx, nxt = i % 3, (i+1) % 3

    M[idx], M[nxt] = max(M[idx] - (C[nxt] - M[nxt]),  0), min(C[nxt], M[nxt]+M[idx])

for i in M:
    print(i)