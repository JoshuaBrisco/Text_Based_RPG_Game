#---imports 
import math, pandas as pd, numpy as np, csv

#---objects

class character():
  def __init__(self, name, health, attack, defense) -> None:
    self.name = name 
    self.health = health
    self.attack = attack
    self.defense = defense
    
  def show_current_stats(self) -> None:
    print(f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}" )


class Player(character):
  def __init__(self, name, health, attack, defense, inv) -> None:
    super().__init__(name, health, attack, defense)
    self.inv = inv #will contain a list, initial inv may change based on what class

  def basic_attack(self) -> None:
    print("Basic attack!") # return damage number


class Knight(Player):
  def __init__(self, name, health, attack, defense, inv) -> None:
    super().__init__(name, health, attack, defense, inv)

  def power_ability(self) -> None:
    print("Power attack") 

  def special_ability(self) -> None:
    print("Special attack!")


class Thief(Player):
  def __init__(self, name, health, attack, defense, inv) -> None:
    super().__init__(name, health, attack, defense, inv)


class Vampire(Player):
  def __init__(self, name, health, attack, defense, inv) -> None:
    super().__init__(name, health, attack, defense, inv)


class Enemy(character):
  def __init__(self, name, health, attack, defense) -> None:
    super().__init__(name, health, attack, defense)


#---functions
def intro_to_game() -> None: #introduces the game and asks for the user's name/class/stats
  print("Welcome to Text Based RPG!")
  print()

def create_player() -> None:
  char: str = ""
  name: str = ""
  
  print("Choose your class!")
  print("'K' for Knight | 'T' for Thief | 'V' for Vampire")
  print()
  
  while True:
    char = input("Enter your choice: ")
    if char == "k" or char == "K":
      char = "Knight"
      break
    elif char == "t" or char == "T":
      char = "Thief"
      break
    elif char == "v" or char == "V":
      char = "Vampire"
      break
    else:
      print("Not an appropriate choice, try again!")
  print(f"You chose {char}!")   

  name = input("What is your name: ")

  if char == "Knight":
    player = Knight(name,0,0,0,[])
  elif char == "Thief":
    #player = Thief(name,0,0,0,[])
    print(name)
  elif char == "Vampire":
    #player = Vampire(name,0,0,0,[])
    print(name)
  else:
    print("There is an error")

  print(f"So your name is {name}!")

def display_map(): #shows the map so the user can see where they are
  print("-----------------")


def ask_for_action(): #character movement etc
  print("What would you like to do?")

def return_map_as_list_of_lists():
  map = []
  with open('Map1.csv', 'r') as map_read:
    csvreader = csv.reader(map_read)
    for row in csvreader: 
      map.append(list(row[0])) #list() takes the strings and makes them a list of str

  return map


#---main
if __name__ == "__main__":
 
  print(return_map_as_list_of_lists())
  
  intro_to_game()
  create_player()
  #intro_to_map()
  
  
  #game engine
  
  #while True:
    

#Testing
  
#player = Knight("Josh", 50, 10, 5, [])
#player.showCurrentStats()
#player.powerAttack()