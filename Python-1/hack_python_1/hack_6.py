"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    for i in range(0,6):
        result.append(i)
    print(result)
    return result

r = fn_hack_6()