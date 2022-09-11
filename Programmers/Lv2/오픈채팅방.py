def solution(records):
    answer, tmp = [], []
    # uid_dict = {'uid': [Enter(1)/Leave(0), nickname]}
    # uid_dict = {'uid1234': 1, Muzi]}
    uid_dict = {}
    for rec in records:
        rec = rec.split()
        if rec[0] == 'Leave':
            uid_dict[rec[1]][0] = 0
            tmp.append([rec[1], '님이 나갔습니다.'])
        else:
            if rec[0] == 'Enter':
                uid_dict[rec[1]] = [1, rec[2]]
                tmp.append([rec[1], '님이 들어왔습니다.'])
            elif rec[0] == 'Change':
                uid_dict[rec[1]] = [1, rec[2]]
    for uid, msg in tmp:
        answer.append((uid_dict[uid][1] + msg))
    return answer