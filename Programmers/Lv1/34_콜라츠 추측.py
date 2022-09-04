def solution(num):
    if num == 1:
        return 0
    
    else:
        n = 0
        while num != 1 and n != 500:
            n += 1
            if num % 2:
                num = num * 3 + 1
            else:
                num //= 2
    return -1 if n == 500 else n