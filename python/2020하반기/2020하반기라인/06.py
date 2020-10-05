def solution(companies, applicants):
    answer = []
    apply = set()
    com, app = {}, {}
    for i in range(len(companies)):
        temp = list(map(str, companies[i].split()))
        temp[2] = int(temp[2])
        temp.append([0 for _ in range(len(temp[1]))])
        com[temp[0]] = temp[1:]
        
    for i in range(len(applicants)):
        temp = list(map(str, applicants[i].split()))
        temp[2] = int(temp[2])
        app[temp[0]] = temp[1:]
        apply.add(temp[0])
        
    r = 1 # 라운드
    while(apply):
        # 지원하기
        for p in apply:
            hope_com = app[p][0][0] # p 지원자의 희망 기업
            priority = com[hope_com][0]
            
            for i in range(len(priority)):
                if com[hope_com][2][i] == 0:
                    com[hope_com][2].insert(i,p)
                    break
                elif priority.index(com[hope_com][2][i]) < priority.index(p): 
                    com[hope_com][2].insert(i,p)
                    break
            if p in app and app[p][1] == r:
                del app[p]
            else:
                app[p][0] = app[0][1:]
        
        # 거절하기
        for c in com:
            apply_list = c[2] # 지원자리스트
            num = c[1] # 채용인원수
            for x in apply_list[num:]:
                if x == 0:
                    break
                elif x in app:
                    apply.add(x)
            c[2] = c[:num] + [0]*(len(c[2])-num)
        r += 1
    
    s_com = sorted(com.items())
    for c, p, n, a in s_com:
        a.sort()
        result = c + '_' + ''.join(a[:n])
        answer.append()

        
    return answer

solution(["A fabdec 2", "B cebdfa 2", "C ecfadb 2"],["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"])