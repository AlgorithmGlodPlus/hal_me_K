get_answer = {2:'SUN', 3:'MON', 4:'TUE', 5:'WED', 6:'THU', 0: 'FRI', 1: 'SAT'}
get_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def solution(a, b):
    d = b - 1
    if a > 1:
        for m in range(1, a):
            d += get_day[m]
    answer = get_answer[d%7]
    return answer