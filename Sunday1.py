x = lambda a,b :a*b
print(x(2,3))
print ("_________----________  ")

def x(num):
    print (num)
    if num!=0:
        x(num-1)
x(1)        