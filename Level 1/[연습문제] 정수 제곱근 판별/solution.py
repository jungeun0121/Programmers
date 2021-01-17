import math
# sqrt(x) : x의 제곱근 반환
# modf(x) : x의 (소수, 정수) 반환
# pow(x,y) : x의 y승 반환

def solution(n):

    return math.pow(math.sqrt(n)+1, 2) if n > 0 and math.modf(math.sqrt(n))[0]  == 0 else -1