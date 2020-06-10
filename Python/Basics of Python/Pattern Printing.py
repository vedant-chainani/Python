#PATTERN PRINTING
a=None
b=None
i=0
print("**************************      Welcome to Pattern Printer      **************************\n\n\n")
print("Enter the numer of ROWS you want to print-: ")
a=int(input())
print("Enter 0 for Acending Pattern (or) 1 for Decending Pattern-:")
b=int(input())
if bool(b)==False:
    print('\nHere is yor Pattern')
    for i in range(a+1):
        print("*"*i)
        i=i+1
if bool(b)==True:
    print('\nHere is yor Pattern')
    for i in range(a,0,-1):
        print("*"*i)
        i=i-1

