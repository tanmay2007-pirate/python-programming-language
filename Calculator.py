print("---------------ENTERING THE CALCULATOR ------------------")
while True : 

    a = float (input ("Enter the first integer : "))

    b = float (input("Enter the second integer : "))

    print("-------------MENU OF CHOICES -------------")
    print("\n")
    print("Enter your choice for Operation : ")
    print("Addition = 1 ")
    print("Subtraction = 2")
    print("Multiplication = 3")
    print("Divison = 4 ")
    print("Remainder = 5 ")
    print("Exit to Terminal : 6")
    print("-------------------------------------------")
    print("\n") 
    c = int (input ("enter your choice : "))

    if c==1 :
        print("Addition is : " , a+b)
    elif c==2 :
        print("Subtraction is : ", a-b)
    elif c==3 :
        print("Mulltiplication is : ", a*b)
    elif c==4 :
        print("Divison is : ", a/b)
    elif c==5 :
        print("remainder is : ", a%b)
    elif c==6 :
        break
    else :
        print("\n")
        print(" Enter choices showed in menu : ")
        