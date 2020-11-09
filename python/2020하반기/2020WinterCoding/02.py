from collections import deque

def solution(encrypted_text, key, rotation):
    answer = ''
    deq = deque()
    deq.extend(encrypted_text)
    
    # rotation 값 뒤집기
    rotation = 0 - rotation
    
    # rotation 복호화
    deq.rotate(rotation)
    
    temp = list(deq)
    # key 복호화
    for i in range(len(key)):
        t, k = temp[i], key[i]
        answer += chr( ord('a') + ( ord(t) - ord(k) - 1)%26 )
    

    return answer

##

# en, key, ro = 'qyyigoptvfb', 'abcdefghijk', 3
# ans = 'hellopython'

##

en, key, ro = 'a', 'z', 1
ans = 'a'


print(solution(en, key, ro))
if solution(en, key, ro) == ans:
    print('통과')