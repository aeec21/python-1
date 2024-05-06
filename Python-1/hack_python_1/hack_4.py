"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    res = f"{result[0:7]}{result[7].upper()}"
    return res

r = fn_hack_4()

