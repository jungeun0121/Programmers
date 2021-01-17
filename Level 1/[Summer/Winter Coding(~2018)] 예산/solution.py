def solution(numbers):
    
    answer = []
    
    for idx1, num1 in enumerate(numbers):
        for idx2, num2 in enumerate(numbers[(int(idx1)+1):]):
            answer.append(num1 + num2)
            
    answer = sorted(set(answer))
    
    return answer