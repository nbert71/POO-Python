class Character:
    
    def __init__(self, name, hp):
        self.__name = name;
        self.__hp = hp;

    def getName(self):
        return self.__name
    
    def getHp(self):
        return self.__hp

    def loseHp(self, damage):
        self.__hp -= damage
    
    def gainHp(self, heal):
        self.__hp += heal

    def display(self):
        print(type(self).__name__  + " " + self.getName())
        print('- HP : ' + str(self.getHp()))

        