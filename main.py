#---imports 

#---objects

class charater():
  def __init__(self, name, health, attack, defense):
    self.name = name 
    self.health = health
    self.attack = attack
    self.defense = defense

class Player(charater):
  def __init__(self, name, health, attack, defense):
    super().__init__(name, health, attack, defense)


#---functions
def intro_to_game(): #introduces the game and asks for the user's name/class/stats
  print("Welcome to Text Based RPG!")
  print("What is your name?")
  name = input()

def display_map(): #shows the map so the user can see where they are
  print("-----------------")


def ask_for_action(): #character movement etc
  print("What would you like to do?")

#---main
