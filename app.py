age = input("How old are you: ")
if age != "":
    age = int(age)
    if  age >= 18 and  age < 21:
        print("You can enter but need wristband")
    elif  age >= 21 :
         print("You can enter and drink!")
    else: 
         print("You cant come in little dude =(")
else: 
    print("Please enter an age!")


