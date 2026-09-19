def text(a):
    if len(a)>100:
        return a[:100]+",,,"
    elif len(a)<=100 :
        return a[:100]   
  
t=input ("enter texts: ")
    

show=text(t)    
print (show)

