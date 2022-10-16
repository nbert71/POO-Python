from Character import *

class Dwarf(Character):
    
    def __init__(self, name, hp=80):
        super().__init__(name, hp)
        self.__damage = 20

    def display(self):
        super().display()
        print("- Damage : " + str(self.__damage))

    def attack(self, player):
        player.loseHp(self.__damage)
