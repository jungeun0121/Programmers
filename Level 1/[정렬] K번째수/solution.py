def solution(array, commands):
    
    answer = []
    
    for i in commands:
        answer.append(sorted(array[int(i[0]-1):i[1]])[int(i[2])-1]) 
    
    return answer