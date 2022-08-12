def solution(id_list, report, k):
    answer = [0] * len(id_list)
    bad_user = {}
    
    for id in id_list:
        bad_user[id] = [0, []]
    
    for report in set(report):
        user1, user2 = report.split()
        bad_user[user2][0] += 1
        bad_user[user2][1].append(user1)
    
    for id in id_list:
        if bad_user[id][0] >= k:
            for i in range (len(bad_user[id][1])):
                idx = id_list.index(bad_user[id][1][i])
                answer[idx] += 1
                
    return answer