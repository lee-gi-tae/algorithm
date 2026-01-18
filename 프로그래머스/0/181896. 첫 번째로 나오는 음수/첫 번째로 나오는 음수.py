def solution(num_list):
    for i in range(len(num_list)):
        if num_list[i] <= 0:
            answer = i
            return answer
    
    return (-1)