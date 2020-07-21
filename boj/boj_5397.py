# 키로거
# 스택, 구현, 그리디
# 41 / 40분
# Silver 3

# 시간초과! > 스택 2개로 해결

test_case = int(input())

for _ in range(test_case):
    L = input()
    left = []
    right = []
    for key in L:
        if key == '<':
            if left:
                right.append(left.pop())
        elif key == '>':
            if right:
                left.append(right.pop())
        elif key == '-':
            if left:
                left.pop()
        else:
            left.append(key)

    # left.extend(reversed(right))
    while right: 
        left.append(right.pop())
    print(''.join(left))
