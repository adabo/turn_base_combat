print("Game starts now!\n")
class Entity:
    def __init__(self, Name):
        self.name = Name
        self.isMyTurn = False

player = Entity("Abel")
player.isMyTurn = True
entity_objects = [player]

npc = Entity("Gort")
entity_objects.append(npc)

npc = Entity("Sam")
entity_objects.append(npc)

npc = Entity("Piggy")
entity_objects.append(npc)

npc = Entity("Zax")
entity_objects.append(npc)

toggleNextEntity = False
i = 0

def setNextEntityTurn(object_list):
    global toggleNextEntity

    for entity in object_list:
        if(entity.isMyTurn == True):
            entity.isMyTurn = not entity.isMyTurn
            toggleNextEntity = True
            break


while(i < 20):
    for entity in entity_objects:
        if(entity.isMyTurn == True):
            print("It's ", entity.name, " turn!\n")
    setNextEntityTurn(entity_objects)
