#While Loops


i=0
while(i<10):
    print(i+1,end=" ")
    i=i+1


# BEAK AND CONTINUE
i=0
while(True):
    if i+1<8:
        i=i+1
        continue
    if i<20:
        print(i)
        i=i+1
        break





#choose a number above 100
i=int(input("Enter a Number"))
if i<100:
    while i<100:
        i=int(input())
    print("you have chosen a number above hundred")
else:
    print("the number is already above hundred") 
    



#Exercise 3 Guess the number
a=0
chances=int(input("Enter no of chances -\n"))
n=int(input("ENTER THE NUMBER YOU WANT TO GUESS \n"))
i=int(input("ENTER YOUR FIRST TRAIL GUESS \n"))

if i!=n :
    print("OK TRAIL OVER LETS START ENTER YOU FIRST GUESS")
    while i!=n and a!=chances:
        a=a+1
        inp=int(input("\n"))
        if inp in range(n+8,100000000000000000000000000000000000000000):
             print("you are too far from the number decrease the value")
        if inp in range(n+1,n+8):
            print("you are close go a little lower")
        if inp in range(-100000000000,n-10):
        if inp in range(n-4,n):
            print ("you are very very close go a little bit higher")
        if inp in range(n-10,n-4):
            print ("you are close go  higher")
        if inp==n: 
            print("CONGRATS YOU HAVE GUESED CORRECT NUMBER")
            break
        
print("GAME OVER YOU HAVE USED YOUR ALL chances")






# OPERATORS
# ARITHEMATIC OPERATORS (+,-,*,/,**,%,//)
# ASSIGNMENT OPERATORS (=,+=,-=,*=,/=)
#LOGITAL OPERATORS (and)