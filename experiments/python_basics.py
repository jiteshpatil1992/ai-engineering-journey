class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def introduce(self) -> None:
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Jitesh", 34)
person1.introduce()

person2 = Person("Kajal", 33)
person2.introduce()
