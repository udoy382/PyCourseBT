# magic/dunder method

# a = str(12346)
# string = ['a', 'b', 'c', 'd']
# print(type(a))
# print(len(string))

class Student:
    def __init__(self, roleno, name):
        self.roleno = roleno
        self.name = name

    def __str__(self):
        return "Class str is called"

    def __len__(self):
        return len(self.name)

    def __del__(self):
        print("Student is destroyed")


student = Student(12, "Udoy")
print(str(student))
print(len(student))

# if im use del keyword then call function so return error so use del function for prin some text
del student
# print(student)