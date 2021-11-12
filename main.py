import random
from classes import *

cat_1 = Cat("Cam", 1 ,"Tank")
cat_1.print_status()

def generate_enemy():
    with open('enemy_names.txt', 'r') as file1:
        lines = file1.readlines()
        monster_name = lines[random.randint(0, len(lines)-1)][:-1]
    print(monster_name)
    return Enemy("Tank", random.randint(8, 10), random.randint(2, 3))

enemy1 = generate_enemy()



