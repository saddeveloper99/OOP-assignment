class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak():
        print("크왕")


class Dog(Animal):

    def speak(self):
        print("멍멍")


class Cat(Animal):

    def speak(self):
        print("냐옹")


class Developer(Animal):

    def speak(self):
        print("엉엉")

cat = Cat("나비", 4)
dog = Dog("초코", 3)
dev = Developer("김광운", 25)

Animal.speak()
cat.speak()
dog.speak()
dev.speak()

print(cat.age)
