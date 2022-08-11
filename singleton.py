# class Singleton:
#     __innervar=None
#     class inner:
#         def __init__(self) -> None:
#             self.val = None
#     def __init__(self) -> None:
#         if Singleton.__innervar is None:
#             Singleton.__innervar = Singleton.inner()
#     def __getattr__(self, name):
#         return getattr(self.__innervar, name)
#     def __setattr__(self, name, value):
#         return setattr(self.__innervar, name, value)

# a = Singleton()
# a.val = 6
# print(a.val)
# b = Singleton()
# b.val = 8
# print(a.val)
# print(b.val)

class BetterSingleton:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, BetterSingleton):
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self, a, b) -> None:
        self.__instance.a = a
        self.__instance.b = b

i = BetterSingleton(2,3)
i.data = 1
print(i.a, i.b)
j = BetterSingleton(4,5)
j.data = 2


print(i.data)
print(j.data)
print(j.a, j.b)
print(i.a, i.b)