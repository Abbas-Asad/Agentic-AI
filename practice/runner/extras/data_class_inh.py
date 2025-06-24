from dataclasses import dataclass


@dataclass
class Human:
    name: str
    age: int

    def eat(self):
        return f"{self.name} eats"

@dataclass
class Teacher(Human):
    subject: str
    experience_years: int

    def teach(self):
        return f"{self.name} teaches"

a= Teacher
print(dir(a))