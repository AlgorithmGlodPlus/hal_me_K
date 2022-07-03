from sys import stdin

while True:
    chars = stdin.readline().rstrip()
    stack = []
    isBalanced = False
    # 괄호가 하나도 없는 경우
    if chars == '.':
        break

    for char in chars:
        # 여는 괄호 처리
        if char == '(' or char == '[':
            stack.append(char)

        # 닫는 괄호 처리
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                break

        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                break
    # break를 만나지 않고 for문을 끝까지 돈 경우
    else:
        isBalanced = True

    if isBalanced and not stack:
        print('yes')
    else:
        print('no')