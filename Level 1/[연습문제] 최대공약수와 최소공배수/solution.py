def solution(n, m):
    
    # n, m 약수 구하기
    n_divisor = list(i for i in range(1, n+1) if n % i == 0)
    m_divisor = list(i for i in range(1, m+1) if m % i == 0)
    
    # n, m 최대공약수
    greatest_factor = max(list(set(n_divisor) & set(m_divisor)))
    
    # n, m 최소공배수
    least_multiple = greatest_factor
    for i in (n, m):
        least_multiple *= i // greatest_factor

    return [greatest_factor, least_multiple]