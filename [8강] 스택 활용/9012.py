N = int(input())

for _ in range(N):
    chars = input()
    stack = []
    for char in chars:
        if char == '(':
            stack.append(char)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(char)
    if not stack:
        print('YES')
    else:
        print('NO')