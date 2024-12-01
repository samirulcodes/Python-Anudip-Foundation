# start pattern
# ***
# ***
# ***

# for i in range(1,4,1):
#     for j in range(1,4,1):
#         print("*",end=" ")
#     print()

# 123
# 123
# 123

# for i in range(1,4):
#     for j in range(1,4):
#         print(j,end=" ")
#     print()

# 111
# 122
# 333 

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end=" ")
#     print()

#123
#456
#789

# n=1
# for i in range(1,4):
#     for j in range(1,4):
#         print(n,end=" ")
#         n=n+1
#     print()

# ASCII CODE

# ABC / abc
# DEF / def
# GHI / ghi

# n=1
# for i in range(1,4):
#     for j in range(1,4):
#         print(chr(n+64),end=" ") # for printing capital letter
#         # print(chr(n+96),end=" ") # for printing small letter
#         n=n+1
#     print()
    
# *
# **
# ***

# for i in range(1,4):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
    
    
# 54321
# 4321
# 321
# 21
# 1

# n = 5  # Number of rows

# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end="")
#     print() 

#   54321
#    5432
#     543
#      54
#       5

n = 5  # Maximum number to start with
for i in range(1, n + 1):
    # Print spaces at the beginning of the row
    for k in range(i - 1):
        print(" ", end="")
    # Print the decreasing numbers
    for j in range(n, i - 1, -1):
        print(j, end="")
    # Move to the next line
    print()


#       1
#      1 2
#     1 2 3
#    1 2 3 4
#   1 2 3 4 5
#  1 2 3 4 5 6

n = 6
for i in range(1, n + 1):
    for space in range(n - i):
        print(' ', end='')
    for num in range(1, i + 1):
        print(num, end=' ')
    print()

