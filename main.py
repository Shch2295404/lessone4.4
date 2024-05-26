from abc import ABC, abstractmethod


# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Класс меча
class Sword(Weapon):
    def attack(self):
        return "удар мечом"


# Класс лука
class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self, monster):
        attack_result = self.weapon.attack()
        print(f"Боец наносит {attack_result}.")
        monster.take_damage()


# Класс монстра
class Monster:
    def __init__(self, health: int = 100):
        self.health = health

    def take_damage(self, damage: int = 100):
        self.health -= damage
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self.health} здоровья.")


# Пример использования
if __name__ == "__main__":
    monster = Monster()

    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)

    print("Боец выбирает меч.")
    fighter.fight(monster)

    print("\nБоец выбирает лук.")
    fighter.changeWeapon(bow)
    fighter.fight(monster)
