# MAP

# def cube(x):
#     return x*x*x

# print(cube(2))

# l=[1,2,3,4,5]

#  #normal way
# newL=[]   
# for i in l:
#     newL.append(cube(i))

# # by map
# newL=list(map(cube,l)) 
# print(newL)

# MAP BY LAMDA
lists=[2,3,6,10]
x=list(map(lambda x:x*x*x,lists))
print(x)

# FILTER

# def filter_func(a):
#     return a>3

# l=[1,2,3,4,5] 

# newList=list(filter(filter_func,l))
# print(newList)

# FILTER BY LAMDA

lists2=[2,3,6,10]
y=list(filter(lambda a:a>2,lists2))
print(y)

# check from lists2 which is even
z=list(filter(lambda even:even % 2==0,lists2))
print(z)

# check from lists2 which is odd
d=list(filter(lambda odd:odd % 2!=0,lists2))
print(d)


# REDUCE - must be import first

from functools import reduce
num=[1,2,3,4,5]
# num=[3,3,4,5]  # steps
# num=[6,4,5]
# num=[10,5]
# num=[15]  # reduce

# by nrml function
def mysum(x,y):
    return x + y

sum=reduce(mysum,num)
print(sum)

# bt lamda func
num1=[1,2,3,4,5]

sum1=reduce(lambda x,y:x+y,num1)
print(sum1)
