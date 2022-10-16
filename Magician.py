from Character import *

def checkMana(self, cost):
    if self.getMana() >= cost:
        return True
    else:
        print("Vous n'avez pas assez de mana pour lancer ce sort !")
        return False

class Magician(Character):

    __spellCost = 10

    def __init__(self, name, hp=100):
        super().__init__(name, hp)
        self.__mana = 50
        self.__damage = 10

    def display(self):
        super().display()
        print("- Mana : " + str(self.getMana()))
        print("- Spell cost : " + str(self.__spellCost))
        print("- Damage : " + str(self.__damage))
    
    def getMana(self):
        return self.__mana

    def attack(self, player):
        if checkMana(self, self.__spellCost):
            player.loseHp(self.__damage)
            self.__mana -= self.__spellCost
        else:
            print('Vous gagner 30 points de mana')
            self.__mana += 30
        
    def heal(self):
        if checkMana(self, self.__spellCost):
            self.gainHp(40)
            self.__mana -= self.__spellCost
        
