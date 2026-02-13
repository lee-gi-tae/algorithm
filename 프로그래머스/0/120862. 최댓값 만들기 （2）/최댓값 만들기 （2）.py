def solution(numbers):
    numbers.sort()
    
    # 가장 큰 두 수의 곱
    max_product1 = numbers[-1] * numbers[-2]
    
    # 가장 작은 두 수(음수 두 개)의 곱
    max_product2 = numbers[0] * numbers[1]
    
    return max(max_product1, max_product2)
