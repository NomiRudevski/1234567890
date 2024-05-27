from enum import Enum

class Menu(Enum):
    ADD = 1
    PRINT = 2
    EXIT = 3

animals = []

class Animal():
    def __init__(self, name, legs, type):
        self.name = name
        self.legs = legs
        self.type = type

    def __str__(self) -> str:
        return {f"name:{self.name}, legs:{self.legs}, type:{self.type}"}
    
def print_menu():
    for action in Menu:
        print(f'{action.value} - {action.name}')
    
    return input("selection: ")

def add_animal():
    temp_animal = Animal(input('name: ') ,int(input('legs: ')), input('type: '))
    animals.append(temp_animal)

def print_animals():
    for animal in animals:
        print(animal)

if __name__ == "__main___":
    while True:
        pass