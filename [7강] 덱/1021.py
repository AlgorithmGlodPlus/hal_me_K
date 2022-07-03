from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
targets = list(map(int, stdin.readline().split()))
deque = deque([i for i in range(1, N+1)])
cnt = 0

for target in targets:
    while True:
        if deque[0] == target:
            # 1번 연산
            print(deque)
            deque.popleft()
            break
        else:
            # 2번 연산
            mid = len(deque) // 2
            if deque.index(target) <= mid:
                print(deque, mid)
                deque.rotate(-1)
            # 3번 연산
            else:
                print(deque, mid)
                deque.rotate(1)
            cnt += 1
print(cnt)