"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    count = 5
    
    while True:
        result.append(count)
        count -= 1 
        if count == -1:
            break
    
    print(result)
    return result  


r = fn_hack_7()