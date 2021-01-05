def solution(arr):

    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
    
    else:
        answer = arr.copy()
        answer.remove(min(arr))
        
    # print(answer)

    return answer