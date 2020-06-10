import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("1.Exercise   2.Food\n"))
        if(c==1):
            value=input("Type the Exercise you did:\n")
            with open("vedant-exercise-log.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("\nSuccessfully written")
        elif(c==2):
            value = input("Type the Food you ate:\n")
            with open("vedant-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k==2:
        c=int(input("1.Exercise   2.Food\n"))
        if(c==1):
            value=input("Type the Exercise you did:\n")
            with open("shaurya-exercise-log.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("\nSuccessfully written")
        elif(c==2):
            value = input("Type the Food you ate:\n")
            with open("shaurya-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k==3:
        c=int(input("1.Exercise   2.Food\n"))
        if(c==1):
            value=input("Type the Exercise you did:\n")
            with open("amit-exercise-log.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("\nSuccessfully written")
        elif(c==2):
            value = input("Type the Food you ate:\n")
            with open("amit-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    elif k==4:
        c=int(input("1.Exercise   2.Food\n"))
        if(c==1):
            value=input("Type the Exercise you did:\n")
            with open("kashish-exercise-log.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("\nSuccessfully written")
        elif(c==2):
            value = input("Type the Food you ate:\n")
            with open("kashish-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Successfully written")
    else:
        print("\nEnter a valid character")


def retrieve(k):
    if k==1:
        c=int(input("1.Exercise\n2.Food\n"))
        if(c==1):
            with open("vedant-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("vedant-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==2:
        c=int(input("1.Exercise\n2.Food\n"))
        if(c==1):
            with open("shaurya-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("shaurya-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==3:
        c=int(input("1.Exercise\n2.Food\n"))
        if(c==1):
            with open("amit-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("amit-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k==4:
        c=int(input("1.Exercise\n2.Food\n"))
        if(c==1):
            with open("kashish-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("kashish-food.txt") as op:
                for i in op:
                    print(i, end="")
    
    else:
        print("\nEnter a valid character")
print("Health Management System\n\n ")
a=int(input("1.Save\n2.Read\n"))

if a==1:
    b = int(input("1.Vedant\n2.Shaurya\n3.Amit\n4.Kashish\n"))
    take(b)
else:
    b = int(input("1.Vedant\n2.Shaurya\n3.Amit\n4.Kashish\n"))
    retrieve(b)