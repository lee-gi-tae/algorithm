def solution(my_string, num1, num2):
    # 문자열은 수정이 불가능하므로 리스트로 변환
    my_list = list(my_string)
    
    # 두 인덱스의 문자 교환
    my_list[num1], my_list[num2] = my_list[num2], my_list[num1]
    
    # 다시 문자열로 변환하여 반환
    return "".join(my_list)