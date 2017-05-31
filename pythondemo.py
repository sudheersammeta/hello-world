#assigning string value to x and printing it
x="foo"
print(x)

#assigning interger value to same x and printing it
x =10
print(x)

y = "bar"

z= int(input("enter a value for z : "))
print(z + 10)

#defining a function hello()
def hello():
    print("hello from a function")

# From below line, indentation changed; indicating end of above function.

# This checks if the program is directly run from python prompt
if(__name__ == "__main__" ):

    print("main module")

    #calling the function defined above.
    hello()

    #Printing variables created in different ways
    print("I want to print %d, %s" %(x,y))
    print("I want to print again using curly braces : {} {}".format(x,y))
    print("Simplest of all : ", x,y)

    #data structures in Python

    #1. Creating a list in different ways.
    list1 = []
    list2 = ['foo', 'bar']

    #Observe how list2 and list3 behaves
    list3 = list2

    print(list1)
    print(list2)
    print(list3)

    #Adding values to list
    list1.insert(0,10)
    list1.insert(1,20)

    list2.append('python')

    #Iterating over a list
    for item in list2 :
        print(item)

    #Changes in list2 reflects in list3 as well.
    #Lists are MUTABLE in python
    for item in list3 :
        print(item)


    #2. Creating a tuple
    tuple1 = 'foo','bar'
    tuple2 = tuple1
    tuple1 = 'java', 'python'

    #If you print the above tuples, you observe that tuples are immutable
    #Change in one tuple doesnt affect the other.
    print(tuple1)
    print(tuple2)

    #Demo of for loop
    #Below loop iterates over [1,10) incrementing by 2 at each step.
    #Note that 10
    for i in range(1,10,2):
        print(i)
