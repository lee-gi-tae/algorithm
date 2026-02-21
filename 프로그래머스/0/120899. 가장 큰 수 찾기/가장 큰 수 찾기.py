def solution(array):
    answer = []
    a = max(array)
    answer.append(a)
    for i in range(len(array)):
        if array[i] == a:
            answer.append(i)
    return answer