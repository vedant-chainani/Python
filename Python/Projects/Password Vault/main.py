run=True
while run:
    account=str(input("Enter Account Type:- "))
    uname=str(input("Enter Username:- "))
    emailid=str(input("Enter Email-ID:- "))
    passwd=str(input("Enter Password:- "))
    with open(f"password.txt", "a") as f:
        f.write(f"Account type:{account}\nUsername:{uname}\nEmail-ID:{emailid}\nPassword:{passwd}\n\n")
    a=int(input("1.Continue\t2.Exit"))
    if a==2:
        run=False