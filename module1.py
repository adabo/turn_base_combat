# ====== Functions/Classes ====
class Entity:
    def __init__(self, Name):
        self.name = Name
        self.is_my_turn = False
        self.psyche_points = 0

def setNextEntityTurn():
    toggleNextEntity = False
    for entity in entity_objects:
        if(toggleNextEntity == True):
            entity.is_my_turn = not entity.is_my_turn
            break
        elif(entity.is_my_turn == True):
            print("It's ", entity.name, " turn!\n")
            entity.is_my_turn = not entity.is_my_turn
            toggleNextEntity = True

def hasPsychePoints():
    for entity in entity_objects:
        if(entity.psyche_points > 0):
            return True
# =============================

# ====== Variables ============
entity_objects = []
i = 0
# =============================

# ====== Initialize Game ======
print("Game starts now!\n********************************************************************************")
u_input = ""
while(u_input != "Y" and u_input != "y"):
    player_count = int(input("How many players?: "))
    print("Confirm: ", player_count, " players? (Y)es (N)o")
    u_input = input()

while(i < player_count):
    u_input = input("Enter new player name: ")
    entity_objects.append(Entity(u_input))
    i += 1

entity_objects[0].is_my_turn = True
print("Round ", i + 1, " begin!")
# ===========================

# ====== Game Main ==========
i = 0
while(i < len(entity_objects)):
    if(hasPsychePoints(entity_objects) == True):
        getCombatMove("Restricted")
    else:
        getCombatMove("Unrestricted")

    setNextEntityTurn(entity_objects)
    i += 1
# ===========================