import yaml


class Animal:
    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def call(self):
        print(f"{self.name} can calling!")

    def run(self):
        print(f"{self.name} can running!")


class Cat(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "short hair"

    def catch_mouse(self):
        print(f"{self.name} can catch mouse!")

    def call(self):
        print(f"{self.name} can calling as 'miaomiao'!")


class Dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = "long hair"

    def watch_home(self):
        print(f"{self.name} can watch home!")

    def call(self):
        print(f"{self.name} can calling as 'wangwang'!")


if __name__ == "__main__":
    with open("animal.yaml") as c:
        dcat = yaml.safe_load(c)["default_c"]

    cat = Cat(*dcat.values())
    cat.catch_mouse()
    print(f"猫猫姓名：{cat.name}, 颜色：{cat.color}, 年龄：{cat.age}, 性别：{cat.gender}, 毛发：{cat.hair}")

    with open("animal.yaml")as d:
        ddog = yaml.safe_load(d)["default_d"]
    dog = Dog(*ddog.values())
    dog.watch_home()
    print(f"狗狗姓名：{dog.name}, 颜色：{dog.color}, 年龄：{dog.age}, 性别：{dog.gender}, 毛发：{dog.hair}")
