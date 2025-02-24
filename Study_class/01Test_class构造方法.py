# 构造方法的作用是用来初始化对象的属性的。与00Test_class.py中的实例方法不同，这里的构造方法是__init__方法
class Person:
    name = ""
    age = 0

    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 25)
print(p1.name)
print(p1.age)
