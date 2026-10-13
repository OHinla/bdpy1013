class Person:
    def __init__(self, age):
        self.age = age


age = 50
print("before assignment age={}, age id={}".format(age, hex(id(age))))
age += 1
print("after assignment age={}, age id={}".format(age, hex(id(age))))
p1 = Person(50)
print("before assignment age={}, p1 id={}".format(p1.age, hex(id(p1))))
p1.age += 1
print("after assignment age={}, p1 id={}".format(p1.age, hex(id(p1))))
print(p1.age == age)
print(p1.age is age)
p2 = Person(30)
p3 = Person(30)
print(p2.age == p3.age)
print(p2 is p3)
print(p2 == p3)
