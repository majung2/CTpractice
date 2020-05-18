# 주어진 십진수 양수를 (int 범위) 를 이진수로 바꾸는 코드를 재귀함수를 이용하여 구성하시오

N = int(input())

def tentotwo (n):
    if n//2 == 0:
        return n%2
    else:
        return (10 * tentotwo(n//2)+ n%2)

print(tentotwo(N))