def solution(n, lost, reserve): 
    # 여벌 체육복을 가져온 학생이 도난당할 수 있다는 조건 처리  
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_item in reserve_set:
        if reserve_item-1 in lost_set:
            lost_set.remove(reserve_item-1)
        elif reserve_item+1 in lost_set:
            lost_set.remove(reserve_item+1)
    
    return n - len(lost_set)