from Magician import Magician
from Dwarf import Dwarf


def newPlayer():
    c = input('What is your character ? (D for Dwarf and M for Magician) ').lower()
    n = input("What is its name ? ")
    if c == 'm':
        newLine()
        return Magician(n, 100)
    elif c == "d":
        newLine()
        return Dwarf(n, 80)
    else:
        print('Typing error')
        newPlayer()


def newLine():
    print()

def separator():
    print('-------------------------------------------------------------------')


def turn(player, opponent):
    separator()
    player.display()
    newLine()
    opponent.display()
    newLine()

    a = input("It's " + player.getName() + " turn (A for Attack and H for Heal (if possible)) ").lower()
    if a == 'a':
        player.attack(opponent)
    elif a == 'h' and type(player).__name__ == "Magician":
        player.heal()
    else:
        print('Typing error')
        turn(player, opponent)

def play(player1, player2):
    while player1.getHp() > 0 and player2.getHp() > 0:
        turn(player1, player2)
        if player2.getHp() > 0:
            turn(player2, player1)
    separator()
    player1.display()
    newLine()
    player2.display()
    newLine()
    if player1.getHp() <= 0:
        winner = player2
    else:
        winner = player1
    print(winner.getName() + ' a gagné !')


