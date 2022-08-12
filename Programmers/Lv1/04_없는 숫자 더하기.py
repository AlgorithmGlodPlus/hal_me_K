def solution(numbers):
    check = [0] * 10
    answer = 0
    
    for number in numbers:
        check[number] = 1
        
    for i in range(len(check)):
        if not check[i]:
            answer += i
    
    return answer