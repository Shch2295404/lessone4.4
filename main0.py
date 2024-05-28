# Для того чтобы перенести логику проверки гибели монстра в декоратор `@property.setter`,
# нам нужно внести изменения в класс `Monster`.
# Мы создадим свойство `health` с декораторами `@property` и `@health.setter`,
# где будет содержаться логика уменьшения здоровья и проверки на гибель монстра.
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

    def fight(self, monster, damage: int = 100):
        attack_result = self.weapon.attack()
        print(f"Боец наносит {attack_result}.")
        monster.take_damage(damage)


# Класс монстра
class Monster:
    def __init__(self, health: int = 100):
        self._health = health

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value
        if self._health <= 0:
            print("Монстр побежден!")
        else:
            print(f"У монстра осталось {self._health} здоровья.")

    def take_damage(self, damage: int):
        self.health -= damage


# Пример использования
if __name__ == "__main__":
    monster = Monster()

    sword = Sword()
    bow = Bow()

    fighter = Fighter(sword)

    print("Боец выбирает меч.")
    fighter.fight(monster, damage=30)

    print("\nБоец выбирает лук.")
    fighter.changeWeapon(bow)
    fighter.fight(monster, damage=40)

    print("\nБоец выбирает лук.")
    fighter.changeWeapon(bow)
    fighter.fight(monster, damage=10)

    print("\nБоец выбирает меч.")
    fighter.changeWeapon(sword)
    fighter.fight(monster, damage=20)

    # Теперь логика, связанная с проверкой гибели монстра, находится в сеттере свойства `health`.
    # Благодаря этому, если здоровье монстра изменяется каким-либо другим способом,
    # например, не только через урон от оружия, эта логика все равно будет выполнена.
