def solution(s):
    
    answer = ''
    standard = int(len(s)/2)
    
    if len(s)%2 == 0:
        answer = s[standard-1:standard+1]
    else :
        answer = s[standard]
        
    # print(answer)

    return answer