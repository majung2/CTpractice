# 걸그룹 마스터 준석이
# 딕셔너리, 리스트
# 33분
# Silver 2

N, M = map(int, input().split())
girl_group = {} # 멤버명 : 그룹명

# 멤버:그룹으로 값 모두 넣기
for i in range(N): 
    name = input()
    mem = int(input())
    for i in range(mem):
        girl_group[input()] = name

gg = sorted(girl_group.items())

# 문제 받기
for i in range(M): 
    quiz = input()
    q_type = int(input())
    if q_type == 0:
        for name, team in gg:
            if team == quiz:
                print(name)
    else:
        print(girl_group[quiz])



# 인강풀이
# N, M = map(int, input().split())

# team_mem, mem_team = {},{}

# for i in range(N):
#     team_name, mem_num = input(), int(input())
#     team_mem[team_name] = []
#     for j in range(mem_num):
#         name = input()
#         team_mem[team_name].append(name)
#         mem_team[name] = team_name

# for i in range(M):
#     name, q = input(), int(input())
#     if q:
#         print(mem_team[name])
#     else:
#         for mem in sorted(team_mem[name]):
#             print(mem)


