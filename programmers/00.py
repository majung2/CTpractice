def solution(expression):
    answer = 0
    list = []
    num = 0
    for i in expression: # 분리
        if i in ['-','*','+']:
            if num > 0:
                list.append(str(num))
            list.append(i)
            num = 0
        else:
            num *= 10
            num += int(i)  
    
    def cal(a,b,c,list):
        L = list[:]
        while(L.count(a)>0):
            ind = L.index(a) - 1
            num1 = L.pop(ind)
            num2 = L.pop(ind+1)
            L[ind] = str(eval(num1+a+num2))
        while(L.count(b)>0):
            ind = L.index(b) - 1
            num1 = L.pop(ind)
            num2 = L.pop(ind+1)
            L[ind] = str(eval(num1+b+num2))
        while(L.count(c)>0):
            ind = L.index(c) -1
            num1 = L.pop(ind)
            num2 = L.pop(ind+1)
            L[ind] = str(eval(num1+c+num2))
        return abs(L[0])
            
    result = []
    result.append(cal('*','+','-',list))
    result.append(cal('*','-','+',list))
    result.append(cal('+','*','-',list))
    result.append(cal('+','-','*',list))
    result.append(cal('-','*','+',list))
    result.append(cal('-','+','*',list))
    
    answer = max(result)
    
    return answer