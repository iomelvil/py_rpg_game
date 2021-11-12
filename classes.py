import random

class Cat:
    def __init__(self, c_name, c_level, c_role):
        self.name = c_name
        self.level = c_level
        self.role = c_role
        if c_role == "Tank":
            self.health = 10
            self.attack = 2
        elif c_role == "Fighter":
            self.health = 6
            self.attack = 3

    def print_status(self):
        print(self.name)
        print(self.level)
        print(self.role)
        print(self.health)
        print(self.attack)

    # Getters
    def get_health(self):
        return self.health

    def get_attack(self):
        return self.attack

    def get_name(self):
        return self.name

    # Setters
    def set_health(self, new_health):
        self.health = new_health

    def set_attack(self, new_attack):
        self.attack = new_attack


class Enemy:
    def __init__(self, e_role, e_health, e_attack, e_level=1, e_name=None):
        if e_name == None:
            with open('enemy_names.txt', 'r') as file1:
                lines = file1.readlines()
                e_name = lines[random.randint(0, len(lines) - 1)][:-1]
        self.name = e_name
        self.level = e_level
        self.role = e_role
        self.health = e_health
        self.attack = e_attack


