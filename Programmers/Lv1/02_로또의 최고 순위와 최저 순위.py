lotto_rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

def solution(lottos, win_nums):
    answer = []
    
    if lottos == [0, 0, 0, 0, 0, 0]:
        answer = [1, 6]
    else:
        win, zero = 0, 0
        for lotto in lottos:
            if lotto == 0:
                zero += 1
            elif lotto in win_nums:
                win += 1
            else:
                continue
        answer.append(lotto_rank[win+zero])
        answer.append(lotto_rank[win])
        
    return answer