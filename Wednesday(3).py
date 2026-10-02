print ("if result of your code=False ,try again to enter code! .")
print ("for looking your results enter :(my result).")
print ("_________________")
def txt(text):
    if len(text)<30:
        return text
    return text[:10]+"..."   
i=input ("text: ")
vari1= txt(i)

def check(code):
    if len(code)==4 and code.isdigit ():
        return True 
    return False 
i=input ("code: ")     
vari2=check(i)

i2=input ("do you wanna see your results?: ")
if i2=="yes":
    
    print ("your text: ",vari1)
    print("result of your code:" ,vari2)
else:
    print(" ")