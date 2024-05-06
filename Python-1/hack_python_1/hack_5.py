"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    o= f"{result.replace("o","0")[0:3]}"
    i= f"{result.replace("i","1")[3:5]}"
    a= f"{result.replace("a","@")[5:8]}"
    oia= o+i+a
    return oia  

r = fn_hack_5()
