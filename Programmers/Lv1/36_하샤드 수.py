def solution(x):
    answer = True
    str_x = str(x)
    sum_x = 0
    for num in str_x:
        sum_x += int(num)
    if x % sum_x:
        answer = False
    return answer