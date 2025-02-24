class Person:
    name = ""
    age = 0
    __score = 0  # 私有属性，只能在类内部访问

    # 构造方法
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.__score = score  # 私有属性，只能在类内部访问

    # 公有方法，可以被外部调用
    def get_score(self):
        return self.__score  # 私有属性，只能在类内部访问

    # 私有方法，只能在类内部调用
    def __check_score(self):
        if self.__score < 60:
            print(f"{self.name}的成绩不及格,为{self.__score}分")
        else:
            print(f"{self.name}的成绩及格,为{self.__score}分")

    def say(self):
        print(f"我的名字是{self.name}",end="。")
        self.__check_score()  # 调用私有方法self.__check_score()

# self 参数代表类的实例。当你定义一个类的方法时，self 作为第一个参数自动传递给该方法，它允许你访问属于该实例的属性和其它方法。因此，你不需要（也不应该）将 self.__score 和 self.name
# 作为额外的参数传递给方法，因为它们已经是实例的一部分，可以通过 self 直接访问。

p1 = Person("John", 25, 85)
print(p1.name)
print(p1.age)
# print(p1.__score)  # 报错，因为私有属性，只能在类内部访问
print(p1.get_score())  # 调用公有方法

# 调用私有方法
# p1.__check_score()  # 报错，因为不能调用私有方法
p1.say()  # 调用公有方法

