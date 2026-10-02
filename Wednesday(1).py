def txt(text):
     
    if len(text)<=100:
        return text
    else:
        return text[0:100]+"..." 
t=input ("text: ")        
        
print(txt(t) )       