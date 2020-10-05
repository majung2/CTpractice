# 테트로미노

N, M = map(int, input().split())
tetromino = [0 for _ in range(N)]

for i in range(N):
    tetromino[i] = list(map(int, input().split()))
