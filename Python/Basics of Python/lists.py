l1=[]
option=0
i=0
string=None
a=None
while i<3:
    print("Choose a tool")
    print("1:Add elements in list \n2:Remove last added element \n3:Close")
    option=int(input())
    if option==1:
        print("\nEnter the element you want to add in the list")
        string=str(input("\n"))
        l1.append(string)
        print("Sucessfully added",string,"in the List")
    if option==2:
        print("\nare you sure you want to remove last added element(y/n)")
        a=str(input())
        if a=='y':
            l1.pop()
        if a=='n':
            print("OK")
    print("\nYour new list is-:",l1)
    i=option
   
