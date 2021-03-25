# Polymorphism

class Kali:
    def advantage(self):
        print("More Powerful")
    
    def disadvantage(self):
        print("Resource intenisive")

class Parrot:
    def advantage(self):
        print("Lighweight")
    
    def disadvantage(self):
        print("Small community")

kali = Kali()
parrot = Parrot()
kali.advantage()
parrot.advantage()
parrot.disadvantage()

for object in [kali, parrot]:
    print(type(object))
    object.advantage()
    object.disadvantage()

# normal # Polymorphism
'''
def sum(a, b=10):
    return a+b

print(sum(10))
'''