def solution(s):
    answer = []
    words = list(s.split(' '))
    for word in words:
        tmp = ''
        for i in range(len(word)):
            if i % 2:
                tmp += word[i].lower()
            else:
                tmp += word[i].upper()
        answer.append(tmp)
    answer = ' '.join(answer)
    return answer