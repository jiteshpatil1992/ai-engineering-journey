from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    email: str

greet = Person(
    name="Alice", 
    age=30, 
    email="alice@example.com"
)

print(greet)
print(f"Name: {greet.name}, Age: {greet.age}, Email: {greet.email}")