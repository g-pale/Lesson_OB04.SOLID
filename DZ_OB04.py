from abc import ABC, abstractmethod

# Шаг 1: Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

# Шаг 2: Конкретные типы оружия
class Sword(Weapon):
    def attack(self) -> str:
        return "наносит удар мечом"

class Bow(Weapon):
    def attack(self) -> str:
        return "стреляет из лука"

# Дополнительно — можно легко добавить новое оружие, не трогая остальной код
class Axe(Weapon):
    def attack(self) -> str:
        return "бьёт топором"

# Шаг 3: Класс Fighter
class Fighter:
    def __init__(self, name: str):
        self.name = name
        self.weapon: Weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {weapon.__class__.__name__.lower()}.")

    def attack(self, monster):
        if not self.weapon:
            print(f"{self.name} безоружен и не может атаковать!")
            return
        print(f"{self.name} {self.weapon.attack()}.")
        monster.take_damage()

# Класс Monster
class Monster:
    def __init__(self, name: str):
        self.name = name
        self.is_alive = True

    def take_damage(self):
        print(f"{self.name} побеждён!")
        self.is_alive = False

# Шаг 4: Демонстрация боя
if __name__ == "__main__":
    fighter = Fighter("Боец")
    monster1 = Monster("Монстр 1")
    monster2 = Monster("Монстр 2")

    sword = Sword()
    bow = Bow()

    fighter.change_weapon(sword)
    fighter.attack(monster1)

    fighter.change_weapon(bow)
    fighter.attack(monster2)