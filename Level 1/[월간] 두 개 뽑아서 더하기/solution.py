def solution(d, budget):
    
    request = sum(i for i in d)
      
    for i in sorted(d, reverse=True):
        if request > budget:
            d.remove(i)
            request -= i
    
    return len(d)