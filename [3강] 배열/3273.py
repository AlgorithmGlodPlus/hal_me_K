n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        if x == arr[i] + arr[j]:
            cnt += 1
print(cnt//2)