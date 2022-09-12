def solution(s):
    answer = len(s)
    for n in range(1, len(s)//2+2):
        res = ''
        char = s[:n]
        cnt = 1
        for i in range(n, len(s), n):
            if char == s[i:i+n]:
                cnt +=1
            else:
                res += str(cnt) + char if cnt >= 2 else char
                char = s[i:i+n]
                cnt = 1
        res += str(cnt) + char if cnt >= 2 else char
        answer = min(answer, len(res))
    return answer