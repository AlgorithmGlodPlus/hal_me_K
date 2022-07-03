A = int(input())
B = int(input())
C = int(input())
cnt = [0 for _ in range(10)]
res = str(A * B * C)

for num in res:
    cnt[int(num)] += 1

for i in cnt:
    print(i)