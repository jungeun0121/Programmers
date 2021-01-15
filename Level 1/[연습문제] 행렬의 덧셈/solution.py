import numpy as np

def solution(arr1, arr2):

    col = np.array(arr1).shape[0]
    row = np.array(arr1).shape[1]
    answer = np.zeros((col, row)).tolist()
    
    for c in range(0, col):
        for r in range(0, row):
            answer[c][r] = arr1[c][r] + arr2[c][r]
        
    return answer