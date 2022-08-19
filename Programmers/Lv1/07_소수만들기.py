from itertools import combinations

def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))
    for comb in combs:
        num = sum(comb)
        if is_prime_num(num):
            answer += 1
    return answer