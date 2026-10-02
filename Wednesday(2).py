def codeposti(code):
    if len(code)==15 :
        if code.isdigit():
            return True 
    return False
c=input("code: ") 
print(codeposti(c))