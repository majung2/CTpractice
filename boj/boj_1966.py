# 프린터 큐
# 큐, 구현, 그리디
# 60 / 25분
# Silver 3

test = int(input())
result = []

for i in range(test):
    N, M = map(int, input().split())
    doc = list(map(int,input().split()))
    count = 1
    while doc:
        if doc[0] >= max(doc):
            doc.pop(0)
            if M == 0:
                result.append(count)
                break
            else:
                count+=1
                M-=1                    
        else:
            doc.append(doc.pop(0))
            if M == 0:
                M = len(doc)-1
            else:
                M-=1           


# 인강풀이

test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int,input().split()))
    queue = list(map(int, input().split()))
    queue = [(i,idx) for idx, i in enumerate(queue)]

    count = 0
    while True:
        if queue[0][0] = max(queue, key=lambda x: x[0])[0]:
            count +=1
            if queue[0][1]==m:
                print(count)
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))
