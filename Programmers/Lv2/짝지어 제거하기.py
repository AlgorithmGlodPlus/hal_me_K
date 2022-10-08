def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])
    answer = 0 if stack else 1
    return answer