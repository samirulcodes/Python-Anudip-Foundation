# To store the data permanently. Read data from file and write data into the file
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode. ('filename','mode'--- r,w,a)
# r - read (default)
# w - write
# a - append
# x - Create
#rb - binary

# READ

# file=open('FileHandling/myFile.txt')  # no need for r mode bcause r is default
# file=open('FileHandling/myFile.txt','r')
# print(file)  # this will not show exact text
# text=file.read()   # read-- function read all the text
# print(text)
# file.close()


# WRITE

# file=open('FileHandling/myFile.txt','w')
# file.write("Hello World")  # Hello World text will written on myFile.txt
# file.close()


# APPEND

# file=open('FileHandling/myFile.txt','a')
# file.write(" Hello World ")  # Hello World text will append on myFile.txt and jitni baar run krenge utni baar text append hota jayega
# file.close()


# ANOTHER METHOD

# not mandatory to close() when using with function

# read
# with open('FileHandling/myFile.txt','r') as file:
#     print(file.read())
#     file.close()  


# write
# with open('FileHandling/myFile.txt','w') as file:
#     file.write(" Heyy! how are you ")
#     file.close()



# append
# with open('FileHandling/myFile.txt','a') as file:
#     file.write(" Heyy! how are you ")


# Count(read) total no. of line in a file

# file = open("FileHandling/myFile.txt","r")
# file.read()
# count=0
# for l in file:
#     count +=1
# print(count)
# file.close()


# with open('FileHandling/myFile.txt', 'r') as file:
#     lines = file.readlines()
# totalLines = len(lines) 
# print(f'Total number of lines: {totalLines}')


# Count(read) total no. of character in a file

# with open('FileHandling/myFile.txt', 'r') as file:
#     lines = file.read()
#     totalChar = len(lines)

# print(f"Total number of characters: {totalChar}")


# Wap to copy one file to another.


with open('FileHandling/myFile.txt', 'r') as copyFile:
    # print(copyFile.read()) 
    with open('FileHandling/myFile1.txt', 'w') as pasteFile:
        for line in copyFile:
            pasteFile.write(line) 



    



    