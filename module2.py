class Entity:
    def __init__(self, Name):
        self.name = Name
        self.move = ""
        self.is_my_turn = False
        self.psyche_points = 0

def setNextEntityTurn(ObjIndex):
    global entity_objects
    if(ObjIndex + 1 == len(entity_objects)):    # If last object in list
        entity_objects[ObjIndex].is_my_turn = False
        entity_objects[0].is_my_turn = True
    else:
        entity_objects[ObjIndex].is_my_turn = False
        entity_objects[ObjIndex + 1].is_my_turn = True

def getCurrentPlayerTurn():
    global entity_objects
    for entity in entity_objects:
        if(entity.is_my_turn == True):
            return entity

def getCombatMove(Restriction):
    combat_choice = ""
    if(Restriction == "Restricted"):
        combat_choice = input('''
            1. Mele
            2. Range
            Choice: ''')
    elif(Restriction == "Unrestricted"):
        combat_choice = input('''
            1. Mele
            2. Range
            3. Psyche
            Choice: ''')

    if(combat_choice == '1'):
        return "Mele"
    elif(combat_choice == '2'):
        return "Range"
    elif(combat_choice == '3'):
        return "Psyche"

def hasPsychePoints(Player):
    return Player.psyche_points > 0

def resolvePsychePoints(Attacker):
    Attacker.psyche_points -= 1
    print(Attacker.psyche_points, " points remaining.")

# --- Game Setup ---
entity_objects = []
i = 0
while(i < 5):
    u_input = input("Enter new player name: ")
    entity_objects.append(Entity(u_input))
    i += 1
print("")

entity_objects[0].is_my_turn = True

# --- Game ---
i = 0
while(i < 20):
    current_player = getCurrentPlayerTurn()
    print("It's", current_player.name, "'s turn!")
    if(hasPsychePoints(current_player) == True):
        current_player.move = getCombatMove("Restricted")
        resolvePsychePoints(current_player)
        if(current_player.psyche_points == 0):
            setNextEntityTurn(entity_objects.index(current_player))
    else:
        current_player.move = getCombatMove("Unrestricted")
        if(current_player.move == "Psyche"):
            current_player.psyche_points = 3
        setNextEntityTurn(entity_objects.index(current_player))
    print(current_player.name, "chose:", current_player.move, '\n')
    i += 1