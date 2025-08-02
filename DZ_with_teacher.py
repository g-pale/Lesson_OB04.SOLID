from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print(f'боец наносит удар')

class Bow(Weapon):
    def attack(self):
        print(f'боец стреляет из лука')

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())


class Monster():
    pass

sword = Sword()
bow = Bow()

fighter = Fighter(Sword())
fighter.fight()
fighter.change_weapon(bow)
fighter.fight()























