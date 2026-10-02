
sam=0
nu=0
while True:
    x=float(input("enter numbers: "))
    if x==0:
        break    
    sam+=1
    nu+=x
    aver=nu/sam
    
print ("average: ",aver)
print ("sum: ",nu)