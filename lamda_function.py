# lamda function
# filter
# check age greater than 18 using filter lamda function
# ages=[10,18,20,32,13]
# res=list(filter(lambda age: age> 18,ages))
# print(res)

# map
# multiply each element by two
# data=[10,18,20,32,13]
# res=list(map(lambda n:n*2,data))
# print(res)

# wap to change case
# name=["aman","samirul","harry"]
# res=list(map(lambda a:a.upper(),name))
# print(res)


# lamda function cwh


# def mul(x):
#     return x*2

# same by lamda
mul=lambda x:x*2
cube=lambda n:n*3
avg=lambda x,y,z:(x+y+z)/3

print(mul(2))
print(cube(3))
print(avg(2,4,6))

# passing function in function
def appl(fx,val):
    return 4 + fx(val)

# print(appl(cube,2)) # passing function in function
print(appl(lambda n:n*n*n,2))   # 2*2*2 + 4=12  ---same by lamda function
print(appl(lambda n:n*n,2))   # 2*2 + 4=8      -----same by lamda function