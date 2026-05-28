# # Exception Handling
# try:
#     a= 10
#     b= 0

#     print(a/b)

# except:
#    print("Error Occurred")
   
#  Handling Specific Exceptions  

# try:
#     num = int(12)

# except ValueError:
#     print("Error..!")   

# Using Multiple Except Blocks
# try:
#     a= 10
#     b= 10

#     print(a/b)

# except ZeroDivisionError:
#    print("ZeroDivisionError Occurred")

# except TypeError:
#     print("TypeError Occurred")

# else Block

# try:
#     a= 10
#     b= 10

#     print(a/b)  #backend

# except ZeroDivisionError:
#    print("ZeroDivisionError Occurred")

# except TypeError:
#     print("TypeError Occurred")

# else:
#     print("No exception")

# finally Block

# finally always executes whether an exception occurs or not.

# try:
#     a= 10
#     b= 10

#     print(a/b)  #backend

# except ZeroDivisionError:
#    print("ZeroDivisionError Occurred")

# except TypeError:
#     print("TypeError Occurred")

# else:
#     print("No exception_else")

# finally:
#     print("No exception_finally")



# try:
#    num = int(input("Enter num.."))

#    print(100/num)  #backend

# except ZeroDivisionError:
#    print("ZeroDivisionError Occurred")

# except TypeError:
#     print("TypeError Occurred")

# except ValueError:
#     print("ValueError Occurred")

# else:
#     print("No exception_else")

# finally:
#     print("No exception_finally") 




# name = str(input("Enter You'r Name \n"))

 
# grt = "Welcome" 

# print(name +" "+ grt )