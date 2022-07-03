from sys import stdin

N = int(stdin.readline())
cnt = 0
for _ in range(N):
    chars = stdin.readline().rstrip()
    stack = []
    for char in chars:
        # stack이 비었거나 stack의 마지막 알파벳과 다른 경우
        if not stack or char != stack[-1]:
            stack.append(char)
        # stack이 있으면서 stack의 마지막 알파벳과 일치하는 경우
        else:
            stack.pop()
    # for문을 돈 이후에 스택이 비었다면 cnt += 1
    if not stack:
        cnt += 1
print(cnt)