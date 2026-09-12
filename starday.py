def welcome (name,age,city="kabul"):
    print("welcome",name)
    if name == "mahdi":
        print ("welcome again sir!")
    print ("your age: ",age)   
    if age >18:
        print ("welcome adult scientist")
    print ("city: ",city)   
    if city =="behsod":
        print ("welcome behsodi")        
welcome ("ali",19, "behsod")