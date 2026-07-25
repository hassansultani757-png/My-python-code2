#a=5
#while a>0:
#    print(a)
#   a -=1
#for i in range(9):
#    print ("[",i,"]")
    
#  print("else")  

num=int(input("num: "))
for j in range(2,num):
    for i in range(2,j):
        if j%i==0:
            break
        else:
            print(j)   