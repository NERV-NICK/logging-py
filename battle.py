from random import randint, choice
import logging

logging.basicConfig(filename='battle.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Warrior:
    __START_HP = 100

    def __init__(self, name):
        self.name = name
        self.hp = self.__START_HP
        self.min_damage = 10
        self.max_damage = 15

    def __str__(self):
        return f"{self.name}[{self.hp}]"

    def attack(self, other):
        if isinstance(other, Warrior):
            damage = randint(self.min_damage, self.max_damage)
            other.hp -= damage
            print(f"{self} ударил на {damage} -> {other}")
            logging.info(f"{self} ударил {other} на {damage} единиц здоровья")
        else:
            raise TypeError("Не работает с этим типом")

def fight(list_warriors: list[Warrior]):
    if len(list_warriors) < 2:
        return -1
    while True:
        if len(list_warriors) <= 1:
            return list_warriors
        random_attacker = choice(list_warriors)
        random_defender = choice([war for war in list_warriors if war != random_attacker])
        random_attacker.attack(random_defender)
        if random_defender.hp <= 0:
            list_warriors.remove(random_defender)

if __name__ == '__main__':
    w1, w2, w3, w4, w5 = Warrior("1"), Warrior("2"), Warrior("3"), Warrior("4"), Warrior("5")
    print(*fight([w1, w2, w3, w4, w5]))
