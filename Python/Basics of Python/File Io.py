#FILE IO BASICS

"""
                    "r" - Open file for reading -default
                    "w" -open file for writing
                    "x" -creates file if not exists
                    "a" - add more content to file
                    "t" -text mode -default
                    "b" -binary mode
                    "+"DLLs
"""


# opening file

f=open("vedant.txt","r")       # "rt" is dafault mode "rb" means read in binary
content=f.read()               # inside the () it specifies no of characters
print(content)
f.close()                      #always remember to close a file after opening



# reading a line
f=open("vedant.txt","r")
print(f.readline())
print(f.readline())

#read all lines
print(f.readlines(),end=" ")   # makes a list of all lines


# replacing the full text document with another text
f=open("vedant.txt","w")
f.write("write the text you want to add")
f.close()

#appending text in a file
f=open("vedant.txt","a")
f.write("write the text you want to append")
f.close()


#read and write both
f=open("vedant.txt","r+")
print(f.read())


#More on File IO
f=open("vedant.txt")
print(f.readline())       #read line
print(f.tell())           # tells us on which character my pointer is on
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(26)            	  #moves the pointer to a specified character
print(f.readline())
print(f.tell())


#with block


with open("vedant.txt") as f:           # this is a alternative to -----    f=open("vedant.txt")
    print(f.readline())                 #                                   f.close()

