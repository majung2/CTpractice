# 보너스 점수
# Bronze 2

N, S = int(input()), input()

bonus, score = 0, 0

for i in range(N):
    if S[i] == 'O':
        score += (i+1) + bonus
        bonus += 1
    else:
        bonus = 0

print(score)
