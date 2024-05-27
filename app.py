from enum import Enum

class Menu(Enum):
    ADD = 1
    PRINT = 2
    EXIT = 3

class Animal():
    def __init__(self, name, legs, type):
        self.name = name
        self.legs = legs
        self.type = type

    def __str__(self) -> str:
        return {f"{self.name}, {self.legs}, {self.type}"}

animal1 = Animal('bob', 4, 'cat')
animal2 = Animal('petunia', 2, 'ostridge')
animal3 = Animal('robert', 8, 'spider')

if __name__ == "__main___":
    pass