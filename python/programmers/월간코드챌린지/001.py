def solution(numbers):
    answer = []
    num_sum = set()

    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            num_sum.add(numbers[i]+numbers[j])
    
    answer = list(num_sum)
    answer.sort()

    return answer