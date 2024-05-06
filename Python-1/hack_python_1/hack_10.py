"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    for _ in result:
        res = list(result.replace("o","0").replace("i","1").replace("a","@").upper())   
    return res

r = fn_hack_10()
print(r)
