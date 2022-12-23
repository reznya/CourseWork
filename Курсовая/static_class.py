class StaticClass:
    key = 3
    @classmethod
    def g(cls, arg):
        # here we can use 'cls' instead of the class name (Test)
        if arg > cls.i:
            cls.i = arg

print(StaticClass.key)
t = StaticClass()

t.key = 5
u = StaticClass()
print(u.key)