def solution(seoul):
    answer = ''
    for x in range(len(seoul)):
        if seoul[x] == 'Kim':
            answer = f'김서방은 {x}에 있다'
            break
    return answer