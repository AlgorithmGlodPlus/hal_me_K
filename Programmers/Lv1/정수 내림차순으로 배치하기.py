def solution(n):
    s = sorted(list(str(n)), reverse=True)
    return int(''.join(s))