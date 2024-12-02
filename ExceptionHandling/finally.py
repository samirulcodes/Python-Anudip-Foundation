def func():
    try:
      l=[1,2,3,4]
      i=int(input("Enter number "))
      print(f"Value at index {i} is {l[i]}")
      return 1
    except:
      print('some error occurred')
      return 0
  
    finally:
        print("I am always executed, either try will execute or except will execute no matter")
    
x=func()
print(x)