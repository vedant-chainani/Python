#Try Except Handling

def tryexcepthandling():
    num1=input("enter num 1 \n")
    num2=input("enter num 2")
    try:
        print("the sum of these two numbersis  ",
              int(num1)+int(num2))
    except Exception as e:
        print(e)
    print("this is very important")

tryexcepthandling()