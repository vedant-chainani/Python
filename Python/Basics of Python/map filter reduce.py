numbers=['54','25','1']
print(type(numbers[1]))
#to convert these string to numbers
def string_to_num():
    for i in range(len(numbers)):
        numbers[i]=int(numbers[i])
        
    print(type(numbers[1]))



#alternative map func
#Syntax---   map(type,function)


def map_function():
    numbers=list(map(int,numbers))
    num=[2,3,4,5,6,7,8,9]
    def sq(a):
        return a**2
    squares=list(map(sq,num))
    print(squares)

    num=[2,3,4,5,6,7,8,9]
    squares=list(map(lambda x: x*x,num))
    print(squares)


def map_function2():
    num=[2,3,4,5,6,7,8,9]
    def sq(a):
         return a**2
    def cube(a):
         return a**3

    func=[sq,cube]
    for i in range(5):
        val=list(map(lambda x:x(i),func))
        print(val)


#Filter func
def filter_function():
    num=[1,2,3,4,5,6,7,8,9,10,11,25]
    def greater_than_5(a):
        return a>5
    gr_than_5=list(filter(greater_than_5,num))
    print(gr_than_5)
    
# reduce function
def reduce_function():
    from functools import reduce
    list1=[1,2,3,4,25,45]
    num=reduce(lambda x,y:x+y,list1)
    print(num)
reduce_function()


























    