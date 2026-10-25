def calculator():
    try:
       num1 = float(input("enther the fist number: "))
       operator = input("enther oparator( + , -, *, / )")
       num2 = float(input("enther the second number: "))

       if operator == "+":
         print("reslut:",num1 + num2)

       elif operator == "-":
           print("reslut:",num1 - num2)

       elif operator == "*":
            print("reslut:",num1 *num2)

       elif operator == "/":
           if num2 != 0:
             print("reslut:",num1 / num2)
           else:
             print("cannot divide by zero")
       else:
         print("invaild operator")
    
    except ValueError:
           print("please enter valid numbers")

    finally:
        print("calculator succssful")

calculator()

