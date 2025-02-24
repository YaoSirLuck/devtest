class Person:
    name = ""
    age = 0

    # 构造方法
    def __init__(self):
        pass

    # 构造类的成员方法
    def say(self):
        print(f'我的名字是{self.name},我今年{self.age}。')

    def say2(self, msg):
        print(f'我的名字是{self.name},我今年{self.age}。备注：{msg}')


zhangsan = Person()
lisi = Person()
zhangsan.name = "张三"
zhangsan.age = 20
lisi.name = "李四"
lisi.age = 25
print(zhangsan.name, zhangsan.age)
print(lisi.name, lisi.age)

wangwu = Person()
wangwu.age = 22
wangwu.name = "王五"
wangwu.say()
wangwu.say2("我未成年，请多关照。")

print("测试git")
