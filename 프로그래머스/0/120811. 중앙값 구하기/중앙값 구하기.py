def solution(array):
    a = (len(array) // 2)
    array.sort()
    answer = array[a]
    return answer