game_state = {
    "player": {
        "name": "Bob", 
        "level": 20
    },
    "weapon": {
        "type": "axe", 
        "level": 4, 
        "damage": 20
    },
    "position": {
        "x": 100, 
        "y": 200
    },
    "encounter_chance": 0.20,
}

class Player:
    def __init__(self, name, level=0):
        self.name=name
        self.level=level
    # other player behaviors

class Weapon:
    def __init__(self, name, level=0, damage=None):
        self.name=name
        self.level=level
        self.damage=damage

# class GameState ...

def step(xmovement, ymovement, state) -> None:
    """
    Takes a step
    
    Moves some (x, y) amount and modifies the game state
    """
    ...

def take_step(x, y) -> dict:
    """ 
    Takes a step
    
    Moves some (x, y) amount and returns a new game state
    """
    ...