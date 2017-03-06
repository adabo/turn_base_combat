import random
class Entity:
    def __init__(self, Name, IsMyTurn):
        self.name = Name
        self.is_my_turn = IsMyTurn
        self.move = ""
        self.psyche_moves = 0

# ---- Functions --- #
def swapTurns():
    global player
    global npc
    player.is_my_turn = not player.is_my_turn
    npc.is_my_turn = not npc.is_my_turn

def hasBuffPoints(Attacker):
    return Attacker.psyche_moves > 0

def chooseCombatMove(Attacker):
    if(hasBuffPoints(Attacker)):
        rand = random.randint(1, 2)
        if(rand == 1):
            Attacker.move = "Range"
            print(Attacker.name, " chose ", Attacker.move)
        elif(rand == 2):
            Attacker.move = "Mele"
            print(Attacker.name, " chose ", Attacker.move)
    else:
        rand = random.randint(1, 3)
        if(rand == 1):
            Attacker.move = "Range"
            print(Attacker.name, " chose ", Attacker.move)
        elif(rand == 2):
            Attacker.move = "Mele"
            print(Attacker.name, " chose ", Attacker.move)
        else:
            Attacker.move = "Psyche Up"
            print(Attacker.name, " chose ", Attacker.move)
            Attacker.psyche_moves = 3

def doCombatMove(Attacker):
    print(Attacker.name, " does a ", Attacker.move, " move!")

def resolveBuff(Attacker):
    Attacker.psyche_moves -= 1
    print(Attacker.name, " uses a psyche point. Psyche points remaining = ", Attacker.psyche_moves)
# ------------------ #

# ---- Variables --- #
player = Entity("Abel", False)
npc = Entity("Mawg", False)
i = 0
# ------------------ #

# ---- Initialze --- #
rand = random.randint(0, 1)
if(rand == 0):
    player.is_my_turn = True
else:
    npc.is_my_turn = True
# ------------------ #

while(i < 30):
    if(player.is_my_turn == True):
        print("It's ", player.name, "'s turn!")
        if(hasBuffPoints(player) == False):
            chooseCombatMove(player)
            if (player.move != "Psyche Up"):
                doCombatMove(player)
            swapTurns()
        else:
            chooseCombatMove(player)
            doCombatMove(player)
            resolveBuff(player)
            if(hasBuffPoints(player) == False):
                swapTurns()
    else:
        print("It's ", npc.name, "'s turn!")
        if(hasBuffPoints(npc) == False):
            chooseCombatMove(npc)
            if (npc.move != "Psyche Up"):
                doCombatMove(npc)
            swapTurns()
        else:
            chooseCombatMove(npc)
            doCombatMove(npc)
            resolveBuff(npc)
            if(hasBuffPoints(npc) == False):
                swapTurns()

    print("\n")
    i += 1
