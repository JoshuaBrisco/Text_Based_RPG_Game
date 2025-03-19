#---imports 
import csv

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
  def __init__(self, name, health, attack, defense, x_coordinate, y_coordinate, inv) -> None:
    super().__init__(name, health, attack, defense)
    self.x = x_coordinate
    self.y = y_coordinate
    self.inv = inv #will contain a list, initial inv may change based on what class

  def basic_attack(self) -> None:
    print("Basic attack!") # return damage number


class Knight(Player):
  def __init__(self, name, health, attack, defense, x_coordinate, y_coordinate, inv) -> None:
    super().__init__(name, health, attack, defense, x_coordinate, y_coordinate, inv)

  def power_ability(self) -> None:
    print("Power attack") 

  def special_ability(self) -> None:
    print("Special attack!")


class Thief(Player):
  def __init__(self, name, health, attack, defense, x_coordinate, y_coordinate, inv) -> None:
    super().__init__(name, health, attack, defense, x_coordinate, y_coordinate, inv)

class Vampire(Player):
  def __init__(self, name, health, attack, defense, x_coordinate, y_coordinate, inv) -> None:
    super().__init__(name, health, attack, defense, x_coordinate, y_coordinate, inv)


class Enemy(character):
  def __init__(self, name, health, attack, defense) -> None:
    super().__init__(name, health, attack, defense)

class Map():
  def __init__(self):
    self.map = self.map_as_list_of_lists(1) #number passed is which map to start on

  def __str__(self) -> str: #shows map
    pass

  def map_as_list_of_lists(self, map_number) -> list[list]:
    map = []
    with open(f'Map{map_number}.csv', 'r') as map_read:
      csvread = csv.reader(map_read)
      for row in csvread: 
        map.append(list(row)) #list() takes the strings and makes them a list of str

    return map
  
  def return_row_as_string(self, row_list: list[str]) -> str:
    row_string: str = ""
    
    for r in row_list:
      row_string += r

    return row_string
  
  def print_full_map_w_player(self, player) -> None: #need to edit code for player to be in? also need __str__?
    current_row_str = ""
    current_row_index = 0
    
    for row in self.map:
      current_row_str = map.return_row_as_string(row)
      
      if current_row_index == player.y: #this code inserts the player as "P"
        current_row_str = current_row_str[:player.x] + "P" + current_row_str[player.x:]
        
      current_row_index += 1
      print(current_row_str)
      
  def print_visible_area(self, player) -> None:
    visible_row_str = ""
    current_row_index = 0
    
    for row in self.map:
      visible_row_str = map.return_row_as_string(row)

      if current_row_index == player.y: #this code inserts the player as "P"
        visible_row_str = visible_row_str[:player.x] + "P" + visible_row_str[player.x:]
      
      visible_row_str = visible_row_str[(player.x - 5):(player.x + 6)] #HORIZONTAL Vision

      if current_row_index >= player.y - 3 and current_row_index <= player.y + 3: 
        print(visible_row_str) #VERTICAL Vision
      
      current_row_index += 1


#---functions
def intro_to_game() -> None: #introduces the game and asks for the user's name/class/stats
  print("Welcome to Text Based RPG!")
  print()

def create_player():
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

  while True:
    name = input("What is your name: ")
    if name == "":
      print("Please enter a name!")
    else:
      break

  if char == "Knight":
    return Knight(name,0,0,0,20,20,[])
  elif char == "Thief":
    return Thief(name,0,0,0,20,20,[])
  elif char == "Vampire":
    return Vampire(name,0,0,0,20,20,[])
  else:
    print("There is an error")

  print(f"So your name is {name}!")


def ask_for_action(): #character movement etc
  print("What would you like to do?")

def return_map_as_list_of_lists():  #likely should be moved the Map object at some point
  map = []
  with open('Map1.csv', 'r') as map_read:
    csvread = csv.reader(map_read)
    for row in csvread: 
      map.append(list(row)) #list() takes the strings and makes them a list of str

  return map


#---main
if __name__ == "__main__":

  intro_to_game()
  player = create_player()
  map = Map()
  map.print_visible_area(player)
  
  #intro_to_map()
  
  
  #game engine
  
  #while True:
    

#Testing
#player = Knight("Josh", 50, 10, 5, 10, 10, [])
#player.showCurrentStats()
#player.powerAttack()