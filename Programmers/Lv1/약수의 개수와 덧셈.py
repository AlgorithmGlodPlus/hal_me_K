def getDivisorCnt(num):
    cnt = 0
    for i in range(1, num+1):
        if not num % i:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        cnt = getDivisorCnt(num)
        if cnt % 2:
            answer -= num
        else:
            answer += num
    return answer