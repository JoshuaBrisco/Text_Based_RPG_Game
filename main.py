#---imports 
import math

#---objects

class character():
  def __init__(self, name, health, attack, defense):
    self.name = name 
    self.health = health
    self.attack = attack
    self.defense = defense
    
  def showCurrentStats(self):
    print(f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}" )


class Player(character):
  def __init__(self, name, health, attack, defense, inv):
    super().__init__(name, health, attack, defense)
    self.inv = inv #will contain a list, initial inv may change based on what class


class Fighter(Player):
  def __init__(self, name, health, attack, defense, inv):
    super().__init__(name, health, attack, defense, inv)

  def powerAttack(self):
    print("Going for a big attack") #proof of concept, will replace once more of the game engine is in

class Enemy(character):
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

print("Welcome to Text Based RPG!")
print("Choose your class!")

char = input("Enter "f" for figher: ")
#will need error control here for when users enter a wrong input



#Testing
  
#player = Fighter("Josh", 50, 10, 5, [])
#player.showCurrentStats()
#player.powerAttack()