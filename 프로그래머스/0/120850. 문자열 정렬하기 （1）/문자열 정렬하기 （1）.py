def solution(my_string):
    result = []
    
    for ch in my_string:
        if ch.isdigit():
            result.append(int(ch))
    
    result.sort()
    return result

