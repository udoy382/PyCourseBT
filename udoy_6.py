# def func1(a, b):
#     div = 0
#     try:
#         # anything which can produce an exception
#         div = a/b
#     except:
#         print("division by zero caught")
#     else:
#         print("all is well")
#         return div

#     finally:
#         print("this is run anyware")
#     return False

# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# # b = 20

# sum = func1(a, b)
# print(sum)

#-------------------------

try:
    file = open("Hello.txt", "w")
    print(file.read())
except FileNotFoundError:
    print("file not found Exception caught")
except OSError:
    print("not authorize")
except TypeError:
    pass
except TimeoutError:
    pass
finally:
    print("run any way!")