# list1=[1,2,3,4]
# print(list1)
# list1[0]=10
# print(list1)

# lis1=[10,'hello',1.3]
# print(lis1)

# operation
# myList=[1,2,3]
# print(myList[0])

# slicing
# myList=[1,2,3,4,5,6,7,8,9,10]
# print(myList[2:5])
# print(myList[:5])
# print(myList[5:])
# print(myList[::2])

# Methods
# myList=[1,2,3,4]
# myList.append(5)
# print(myList)

# extend
# fruit=['apple','mango','cherry']
# car=['ford','bmw']
# fruit.extend(car)
# print(fruit)

# insert
# myList=[1,2,3]
# myList.insert(1,10)
# print(myList)

# delete methods
fruit=['apple','mango','cherry','pineapple']
rm=['apple','mango']
for i in rm:
    fruit.remove(i)
print(fruit)
# del fruit[1]
# fruit.pop(2)
# fruit.pop(1)
# fruit.remove('apple')
# fruit.remove('mango')
# print(fruit)


# lenght
# fruit=['apple','mango','cherry',['apple','mango','cherry']]
# print(len(fruit))

# type
# fruit=['apple','mango','cherry']
# print(type(fruit))

# in keyw
# fruit=['apple','mango','cherry']
# if "apple" in fruit:
#     print("Yes")

# sort
# fruit=['apple','pineapple','mango','cherry']
# fruit.sort()
# fruit.sort(reverse=True)
# print(fruit)

# inetrnal working
# m=[1,2,3]
# n=[1,2,3]
# print(m==n)
# print(m is n)