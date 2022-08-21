def get_p1(answers):
    p1 = 0
    a1 = [1, 2, 3, 4, 5]
    for i in range(len(answers)):
        if answers[i] == a1[i % 5 if i >= 5 else i]:
            p1 += 1
    return p1

def get_p2(answers):
    p2 = 0
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    for j in range(len(answers)):
        if answers[j] == a2[j % 8 if j >= 8 else j]:
            p2 += 1
    return p2

def get_p3(answers):
    p3 = 0
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for k in range(len(answers)):
        if answers[k] == a3[k % 10 if k >= 10 else k]:
            p3 += 1
    return p3

def solution(answers):
    point = {1: 0, 2: 0, 3: 0}
    point[1] = get_p1(answers)
    point[2] = get_p2(answers)
    point[3] = get_p3(answers)
    answer = [k for k, v in point.items() if v == max(point.values())]
    return answer