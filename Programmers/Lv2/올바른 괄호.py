def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif stack and char == ')':
            stack.pop()
        else:
            return False
    answer = True if not stack else False
    return answer