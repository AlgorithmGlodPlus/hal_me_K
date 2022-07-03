import math
nums = list(map(int, str(input())))
cnt = [0] * 9

for num in nums:
    if num == 6 or num == 9:
        cnt[6] += 0.5
    else:
        cnt[num] += 1

print(math.ceil(max(cnt)))