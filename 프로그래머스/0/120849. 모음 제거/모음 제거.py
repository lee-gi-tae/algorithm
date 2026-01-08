def solution(my_string):
    ban = ["a", "e", "i", "o", "u"]
    answer = ''
    for i in my_string:
        if i not in ban:
            answer += i

            
    return answer