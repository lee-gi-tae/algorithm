def solution(my_string):
    result = ""
    
    for ch in my_string:
        if ch.isupper():          # 대문자라면
            result += ch.lower()  # 소문자로 변환
        else:                     # 소문자라면
            result += ch.upper()  # 대문자로 변환
    
    return result