# SHA-256 : 대표적인 해쉬 알고리즘
# 해시, 구현
# 15분
# Bronze 2

import hashlib

S = input()
sha = hashlib.sha256(S.encode())
print (sha.hexdigest())



