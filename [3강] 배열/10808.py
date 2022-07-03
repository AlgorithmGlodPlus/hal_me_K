chars = input()
cnt = [0 for _ in range(26)]
for char in chars:
    cnt[ord(char) - ord('a')] += 1

print(*cnt)