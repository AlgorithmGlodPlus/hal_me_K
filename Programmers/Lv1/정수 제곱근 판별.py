import math

def solution(n):
    answer = -1
    N = math.sqrt(n)
    is_int = N.is_integer()
    if is_int:
        answer = pow(N+1, 2)
    return answer