#scope global variables,global keywords
l=10   #Global Scope
def function1(n):
   # l=5        #Local Scope Variable
    global l    #if we want to change it then type = "global (variable name)"
    l=l+45      #if a local variable is not found then we cannot change a global variable
   
    m=8
    print(l,m,n,"hiiii")

function1(7)
print("\n",l)