#LISTS IN PYTHON


list1 = [ ["Harry", 1], ["Larry", 2],
          ["Carry", 6], ["Marie", 250]]
dict1 = dict(list1)
for item in dict1:
    print(item)
for item, lollypop in dict1.items():
    print(item, "and lolly is ", lollypop)
items = [int, float, "HaERRY", 5,3, 3, 22, 21, 64, 23, 233, 23, 6]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)
grocery = ["Harpic", "vim bar", "deodrant", "Bhindi",    #this    is a list 
          "Lollypop", 56]
print(grocery[5])      #INDEX PRINTING 
numbers.append(1)      #ADDING NUMBERS
numbers.append(72)
numbers.append(5)
numbers.insert(2, 67)
print(numbers)

print(numbers)
numbers[1] = 98
print(numbers)
#Mutable - can change
#Immutable - cannot change
tp = (1,)
print(tp)
a= 1
b = 8
a, b = b,a
temp = a
a = b
b = temp
print(a, b)



#Dictionary is nothing but key value pairs
d1 = {}     #this is a empty dictionary
print(type(d1))
d2 = {"Harry":"Burger",#      
      "SkillF":"Roti",
      "Shubham":{"B":"maggie", "L":"roti", "D":"Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kebabs"
print(d2)
del d2[420]
print(d2["Shubham"])
d3 = d2.copy()
del d3["Harry"]
d2.update({"Leena":"Toffee"})
print(d2.keys())
print(d2.items())


#QUESTION 1 MAKE A DICTIONARY WITH USER INPUTS


word=str(input("Enter the word for which you want the meaning:"))
dictionary={'word1':'meaning1',
			'word2':'meaning2',
			'word3':'meaning3',
			'word4':'meaning4'}
print(dictionary[word])





#Sets

s = set()                  #defining a set
print(type(s)) 
l = [1, 2, 3, 4]
s_from_list = set(l)          #converting list to set
print(s_from_list)
print(type(s_from_list))
s.add(1)     #adding values
s.add(2)
s.remove(2)         #removing values from sets
s1 = {4, 6}
print(s.isdisjoint(s1))      


