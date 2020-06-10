#IF ELSE AND ELIF CONDITIONS IN PYTHON 
var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print("Greater")
elif var3==var2:
    print("Equal")
else:
    print("Lesser")

list1 = [5, 7, 3]
print(15 not in list1)
if 15 not in list1:
    print("No its not in the list")

#Driving age conformer
def driving(age):
	print("What is your age?")
	age = int(input())
	if age<18:
		print("You cannot drive")

	elif age==18:
		print("We will think about you")

	else:
		print("You can drive")

    



#Exercise 2 Faulty CALCULATOR FOR CHEATING STUDENTS
def faultycalculator(a,b,operator):
	a=int(input('enter first no.-'))
	b=int(input('enter second no.-'))
	operator=str(input('Choose one of the following- (*    /    +    -)-- -'))
	if operator=='*':
		output=a//b
		print(output)
	if operator=='/':
		output=a*b
		print(output)
	if operator=='+':
		output=a**b
		print(output)
	if operator=='-':
		output=a%b
		print(output)
		
		

    
