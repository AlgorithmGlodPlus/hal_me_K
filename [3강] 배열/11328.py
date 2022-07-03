# 메모리 초과
# from itertools import product
#
# T = int(input())
# for _ in range(T):
#     answer = ''
#     str1, str2 = input().split()
#     alpa = []
#     for char in str1:
#         alpa.append(char)
#
#     if str1 == str2:
#         answer = 'Possible'
#
#     elif len(str1) < len(str2):
#         answer = 'Impossible'
#
#     else:
#         words = ["".join(i) for i in list(product(alpa, repeat=len(str1)))]
#         for word in words:
#             if word == str2:
#                 answer = 'Possible'
#                 break
#             answer = 'Impossible'
#     print(answer)


T = int(input())

for i in range(T):
    a, b = input().split()
    a = ''.join(sorted(a))
    b = ''.join(sorted(b))

    if len(a) != len(b):
        print("Impossible")
        continue

    for i in range(len(a)):
        if a[i] != b[i]:
            flag = False
            break
        else:
            flag = True

    if flag:
        print("Possible")
    else:
        print("Impossible")