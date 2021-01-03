def solution(s):
    answer = True
    
    p_num, y_num = 0 , 0
    s = s.lower()    
    # print(s)
    
    for i in s:
        if i =='p':
            p_num += 1
        elif i == 'y':
            y_num += 1
        else :
            continue
    
    if p_num != y_num:
        answer = False
        
    return answer