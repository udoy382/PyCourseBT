# Privacy in Classes

class __Private:
    def __init__(self, a, b):
        # self.__a = a
        self._a = a

        self.b = b
        print("Private class is created")


    def _sum(self):
        # return self.__a + self.b
        return self._a + self.b

priv = __Private(10, 20)
print(priv._sum())
print(priv._a)