# 多态的
class Cat:
    def say(self):
        print("喵喵叫")


class Dog:
    def say(self):
        print("汪汪叫")


def say_something(animal):
    animal.say()


cat = Cat()
dog = Dog()

say_something(cat)  # 喵喵叫
say_something(dog)  # 汪汪叫
