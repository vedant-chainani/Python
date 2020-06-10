from datetime import datetime
# Variables
run=True
lst=[]
program=True
item_list=[]
price_list=[]
quantity_list=[]
finalprice_list=[]
sum=0
count=0
gst=6
vat=6

while run:
    a=str(input("Enter Consumer name: "))
    while program:
        print("Enter in Order-Item Name,Price,Quantity")
        for i in range(3):
            item=input()
            lst.append(item)
        item_list.append(lst[0])
        price_list.append(float(lst[1]))
        quantity_list.append(int(lst[2]))
        finalprice=float(lst[1])*int(lst[2])
        finalprice_list.append(finalprice)
        lst=[]
        print("1.Continue   2.Close")
        close=int(input())
        count+=1
        if close==2:
            program=False
    for l in finalprice_list:
        sum=sum+l
    print("1.Discount\t2.No Discount")
    dischoice=int(input())
    if dischoice==1:
        discount=float(input('Enter Discount Percent:'))
        sum1=(sum)*((100-discount)/100)
        taxsum=sum1+(sum1*(gst/100))+(sum1*(vat/100))
    taxsum1=sum+(sum*(gst/100))+(sum*(vat/100))
    with open(f"{a}.txt", "a") as f:
        f.write(f"Name={a}\n")
        f.write(f"Date of Purchase={datetime.now()}\n")
        f.write("Item\tPrice\tQuantity\tTotal\n")
        for k in range(1):
            for m in range(len(item_list)):
                f.write(f"{m+1}.{item_list[m]}\t{price_list[m]}\t{quantity_list[m]}\t{finalprice_list[m]}\n")
        f.write("-------------------------------\n")
        f.write(f"                              Total={sum}")
        if dischoice==2:
            f.write(f"\n\nTotal price after taxes={taxsum1}")
            f.write(f"\n\nRounded Price={round(taxsum1)}")
        if dischoice==1:
            f.write(f"\n\nDiscount={discount}%")
            f.write(f"\nTotal Price after Discount={sum1}")
            f.write(f"\n\nTotal price after taxes={taxsum}")
            f.write(f"\n\nRounded Price={round(taxsum)}")
    run=False
