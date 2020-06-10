import random
import secrets
import time
init=time.time()
base=''
char1='a b c d e f g h i j k l m n o p q r s t u v w x y z'
char2='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
char3='~ ! @ # $ % ^ & * ( ) _ + { } : " < > ? ` [ ] ; , . /'
char4='1 2 3 4 5 6 7 8 9 0'
symbols=char3.split(' ')
charupper=char2.split(' ')
charlower=char1.split(' ')
numbers=char4.split(' ')
char=symbols+charupper+charlower+numbers
allchar1=list(char)
allchar=allchar1*1024
def shuffle():
    for i in range(len(allchar)):
        j=random.randint(0,i+1)
        allchar[i],allchar[j]=allchar[j],allchar[i]
    #print(allchar)
    
    
def main(length):
    global base
    passwd=random.sample(allchar,length)
    for k in range(len(passwd)):
        base=base+str(passwd[k])
    print(base)
        
shuffle()
time1=time.time()
l=int(input("Enter no of characters: "))
time2=time.time()
main(l)
time3=time.time()
print((time3-time2)+(time1-init))  
