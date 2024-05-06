"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    newresult = []
    contar = len(result)
    i = 0
    while (contar > i):
        a = '@'
        i += 1
        newresult.append(i)
        newresult.append(a)
    return newresult
    
r = fn_hack_9()
