def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num % divisor:
            answer.append(num)
    return sorted(answer) if answer else [-1]