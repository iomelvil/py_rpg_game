class Cat:
    def __init__(self, Cname, Clevel, Crole):
        self.name = Cname
        self.level = Clevel
        self.role = Crole
        if Crole == "Tank":
            self.health = 10
            self.attack = 2
        elif Crole == "Fighter":
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
    def set_health(self, newHealth):
        self.health = newHealth

    def set_attack(self, newAttack):
        self.attack = newAttack



