from sys import stdin
from collections import deque

deque = deque([])
N = int(stdin.readline())

for _ in range(N):
    line = stdin.readline().split()
    order = line[0]

    if order == 'push_front':
        deque.appendleft(int(line[1]))
        print(deque)

    elif order == 'push_back':
        deque.append(int(line[1]))

    elif order == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)

    elif order == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)

    elif order == 'size':
        print(len(deque))

    elif order == 'empty':
        if deque:
            print(0)
        else:
            print(1)

    elif order == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)

    elif order == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)