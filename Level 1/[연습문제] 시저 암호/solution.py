import string

def solution(s, n):
    answer = ''
    
    uppercase = string.ascii_uppercase * 2
    lowercase = string.ascii_lowercase * 2
    # print(lowercase)
    # print(uppercase)
    
    for i in s:
        # print(i)
        
        if i.isupper() == True:
            print(uppercase[uppercase.index(i)+n])
            
            
        elif i.islower() == True:
            print(lowercase[lowercase.index(i)+n])
            
        else:
            print('공백')
    

    return answer