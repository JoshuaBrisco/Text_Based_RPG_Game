# ---imports
import csv
import os
import random

# ---objects


class character:
    def __init__(self, name, health, attack, defense, speed) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.speed = speed

    def show_current_stats(self) -> None:
        print(
            f"Health: {self.health}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}"
        )


class Player(character):
    def __init__(
        self, name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
    ) -> None:
        super().__init__(name, health, attack, defense, speed)
        self.x = x_coordinate
        self.y = y_coordinate
        self.exp = 0
        self.level = 1
        self.inv = (
            inv  # will contain a list, initial inv may change based on what class
        )
        self.skill_choice_made = ["", "", ""]

    def move(self, map) -> None:
        print("W = North | D = East | S = South | A = West")

        while True:
            direction: str = input("Which direction do you move?:")
            if (
                direction.lower() == "n" or direction.lower() == "w"
            ) and map.valid_position(self.x, self.y - 1):
                self.y -= 1
                break
            elif (
                direction.lower() == "e" or direction.lower() == "d"
            ) and map.valid_position(self.x + 1, self.y):
                self.x += 1
                break
            elif (direction.lower() == "s") and map.valid_position(self.x, self.y + 1):
                self.y += 1
                break
            elif (direction.lower() == "a") and map.valid_position(self.x - 1, self.y):
                self.x -= 1
                break
            else:
                print("Not a direction. Try again!")

    def check_for_level_up(self):
        if self.exp >= 1:
            return True
        else:
            return False

    def basic_attack(self) -> None:
        print("Basic attack!")  # return damage number


class Knight(Player):
    def __init__(
        self, name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
    ) -> None:
        super().__init__(
            name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
        )

    def level_up(self):
        self.exp = 0
        self.level += 1
        print(f"You leveled up to level {self.level}!")
        print("Choose a stat to increase!")

        while True:
            level_choice = input(
                "H for Health | A for Attack | D for Defense | S for Speed:"
            )
            if level_choice.lower() == "h":
                self.health += 2
                input("You chose health! Press enter to proceed.")
                break
            elif level_choice.lower() == "a":
                self.attack += 1
                input("You chose attack! Press enter to proceed.")
                break
            elif level_choice.lower() == "d":
                self.defense += 1
                input("You chose defense! Press enter to proceed.")
                break
            elif level_choice.lower() == "s":
                self.speed += 1
                input("You chose speed! Press enter to proceed.")
                break
            else:
                print("Not a valid choice. Try again!")

        if self.level == 5:
            print("1 for Uppercut | 2 for Stun")  # skill choice options at lvl 5
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[0] = "Uppercut"
                    break
                if level_choice == "2":
                    self.skill_choice_made[0] = "Stun"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 10:
            print("1 for Tank Mode | 2 for Bandage")  # skill choice options at lvl 10
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[1] = "Tank Mode"
                    break
                if level_choice == "2":
                    self.skill_choice_made[1] = "Bandage"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 15:
            print("1 for Passive 1 | 2 for Passive 2")  # skill choice options at lvl 15
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[2] = "Passive 1"
                    break
                if level_choice == "2":
                    self.skill_choice_made[2] = "Passive 2"
                    break
                # if level_choice == '3':
                #   self.skill_choice_made[2] = 3
                else:
                    print("Not a valid choice. Try again!")

    def power_ability(self) -> None:
        print(f"You used {self.skill_choice_made[0]}")

    def special_ability(self) -> None:
        print(f"You used {self.skill_choice_made[1]}!")

    def passive_ability(self) -> None:
        print(f"You used {self.skill_choice_made[2]}!")

    def print_skill_options(self) -> None:
        text = "1 for Basic Attack"

        if self.level >= 5:
            text = text + f" | 2 for {self.skill_choice_made[0]}"
        if self.level >= 10:
            text = text + f" | 3 for {self.skill_choice_made[1]}"

        print(text)


class Thief(Player):
    def __init__(
        self, name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
    ) -> None:
        super().__init__(
            name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
        )

    def level_up(self):
        self.exp = 0
        self.level += 1
        print(f"You leveled up to level {self.level}!")
        print("Choose a stat to increase!")

        while True:
            level_choice = input(
                "H for Health | A for Attack | D for Defense | S for Speed:"
            )
            if level_choice.lower() == "h":
                self.health += 2
                input("You chose health! Press enter to proceed.")
                break
            elif level_choice.lower() == "a":
                self.attack += 1
                input("You chose attack! Press enter to proceed.")
                break
            elif level_choice.lower() == "d":
                self.defense += 1
                input("You chose defense! Press enter to proceed.")
                break
            elif level_choice.lower() == "s":
                self.speed += 1
                input("You chose speed! Press enter to proceed.")
                break
            else:
                print("Not a valid choice. Try again!")

        if self.level == 5:
            print(
                "1 for Sneak Attack | 2 for Throw Sand"
            )  # skill choice options at lvl 5
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[0] = "Sneak Attack"
                    break
                if level_choice == "2":
                    self.skill_choice_made[0] = "Throw Sand"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 10:
            print("1 for Bleed Attack | 2 for Evade")  # skill choice options at lvl 10
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[1] = "Bleed Attack"
                    break
                if level_choice == "2":
                    self.skill_choice_made[1] = "Evade"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 15:
            print("1 for Passive 1 | 2 for Passive 2")  # skill choice options at lvl 15
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[2] = "Passive 1"
                    break
                if level_choice == "2":
                    self.skill_choice_made[2] = "Passive 2"
                    break
                # if level_choice == '3':
                #   self.skill_choice_made[2] = 3
                else:
                    print("Not a valid choice. Try again!")

    def power_ability(self) -> None:
        print(f"You used {self.skill_choice_made[0]}")

    def special_ability(self) -> None:
        print(f"You used {self.skill_choice_made[1]}!")

    def passive_ability(self) -> None:
        print(f"You used {self.skill_choice_made[2]}!")

    def print_skill_options(self) -> None:
        text = "1 for Basic Attack"

        if self.level >= 5:
            text = text + f" | 2 for {self.skill_choice_made[0]}"
        if self.level >= 10:
            text = text + f" | 3 for {self.skill_choice_made[1]}"

        print(text)


class Vampire(Player):
    def __init__(
        self, name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
    ) -> None:
        super().__init__(
            name, health, attack, defense, speed, x_coordinate, y_coordinate, inv
        )

    def level_up(self):
        self.exp = 0
        self.level += 1
        print(f"You leveled up to level {self.level}!")
        print("Choose a stat to increase!")

        while True:
            level_choice = input(
                "H for Health | A for Attack | D for Defense | S for Speed:"
            )
            if level_choice.lower() == "h":
                self.health += 2
                input("You chose health! Press enter to proceed.")
                break
            elif level_choice.lower() == "a":
                self.attack += 1
                input("You chose attack! Press enter to proceed.")
                break
            elif level_choice.lower() == "d":
                self.defense += 1
                input("You chose defense! Press enter to proceed.")
                break
            elif level_choice.lower() == "s":
                self.speed += 1
                input("You chose speed! Press enter to proceed.")
                break
            else:
                print("Not a valid choice. Try again!")

        if self.level == 5:
            print("1 for Bite | 2 for Fly")  # skill choice options at lvl 5
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[0] = "Bite"
                    break
                if level_choice == "2":
                    self.skill_choice_made[0] = "Fly"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 10:
            print(
                "1 for Bat Attack | 2 for Shadow Strike"
            )  # skill choice options at lvl 10
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[1] = "Bat Attack"
                    break
                if level_choice == "2":
                    self.skill_choice_made[1] = "Shadow Strike"
                    break
                else:
                    print("Not a valid choice. Try again!")

        if self.level == 15:
            print("1 for Passive 1 | 2 for Passive 2")  # skill choice options at lvl 15
            while True:
                level_choice = input("Pick your new skill: ")
                if level_choice == "1":
                    self.skill_choice_made[2] = "Passive 1"
                    break
                if level_choice == "2":
                    self.skill_choice_made[2] = "Passive 2"
                    break
                # if level_choice == '3':
                #   self.skill_choice_made[2] = 3
                else:
                    print("Not a valid choice. Try again!")

    def power_ability(self) -> None:
        print(f"You used {self.skill_choice_made[0]}")

    def special_ability(self) -> None:
        print(f"You used {self.skill_choice_made[1]}!")

    def passive_ability(self) -> None:
        print(f"You used {self.skill_choice_made[2]}!")

    def print_skill_options(self) -> None:
        text = "1 for Basic Attack"

        if self.level >= 5:
            text = text + f" | 2 for {self.skill_choice_made[0]}"
        if self.level >= 10:
            text = text + f" | 3 for {self.skill_choice_made[1]}"

        print(text)


class Enemy(character):
    def __init__(self, name, health, attack, defense, speed) -> None:
        super().__init__(name, health, attack, defense, speed)


class Map:
    def __init__(self):
        self.map = self.map_as_list_of_lists(
            1
        )  # number passed is which map to start on

    def map_as_list_of_lists(self, map_number) -> list[list]:
        map = []
        with open(f"Map{map_number}.csv", "r") as map_read:
            csvread = csv.reader(map_read)
            for row in csvread:  # row is a list with one item of type string
                map.append(
                    list(row[0])
                )  # list() takes the strings and makes them a list of str

        return map

    def return_row_as_string(self, row_list: list[str]) -> str:
        row_string: str = ""

        for r in row_list:
            row_string += r

        return row_string

    def print_full_map_w_player(
        self, player
    ) -> None:  # need to edit code for player to be in? also need __str__?
        current_row_str = ""
        current_row_index = 0

        for row in self.map:
            current_row_str = map.return_row_as_string(row)

            if current_row_index == player.y:  # this code inserts the player as "P"
                current_row_str = (
                    current_row_str[: player.x] + "P" + current_row_str[player.x + 1 :]
                )

            current_row_index += 1
            print(current_row_str)

    def print_visible_area(self, player) -> None:
        visible_row_str = ""
        current_row_index = 0

        for row in self.map:
            visible_row_str = self.return_row_as_string(row)

            if current_row_index == player.y:  # this code inserts the player as "P"
                visible_row_str = (
                    visible_row_str[: player.x] + "P" + visible_row_str[player.x + 1 :]
                )

            visible_row_str = visible_row_str[
                (player.x - 5) : (player.x + 6)
            ]  # HORIZONTAL Vision

            if current_row_index >= player.y - 3 and current_row_index <= player.y + 3:
                print(visible_row_str)  # VERTICAL Vision

            current_row_index += 1

    def valid_position(self, x, y) -> bool:
        if self.map[y][x] == "." or self.map[y][x] == "t":
            return True
        else:
            return False


class EventManager:
    def __init__(self):
        self.turns_complete = 0
        self.turns_since_last_encounter = 0

    # formatting
    def print_line(self):
        print("----------------------------")

    def clear_terminal(self):
        os.system("cls")

    def print_empty_line():
        print()

    # turn engine
    def complete_turn(self):
        self.turns_complete += 1
        self.turns_since_last_encounter += 1

    def check_for_encounter(
        self, player, map
    ) -> bool:  # player is passed to use its data to adjust the encounter chance
        if map.map[player.y][player.x] == ".":
            location_modifier = 0.3
        elif map.map[player.y][player.x] == "t":
            location_modifier = 0.6
        else:
            location_modifier = 0
        calculated_chance = (
            min(10, self.turns_since_last_encounter) / 10
        ) * location_modifier

        print(f"Location modifier: {location_modifier}")
        print(f"Calculated chance of encounter: {calculated_chance}")

        if random.random() <= calculated_chance:
            return True
        else:
            return False

    def initiate_encounter(self, player, map):

        enemy = create_enemy(map)
        print(f"Encountered a {enemy.name}!")
        self.print_line()

        while True:
            choice = input(
                "Try to run? Enter any key to try to escape or 'F' to fight."
            )  # implement a chance based running system
            if choice.lower() == "f":
                input("You didn't try to escape! Press enter to proceed:")
                break
            else:
                escape_chance = 0.2
                if random.random() <= escape_chance:
                    input("You escaped! Press enter to proceed.")
                    del enemy
                    return
                input("You didnt escape!")
                break

        while True:  # combat loop
            self.clear_terminal()
            print(
                f"{enemy.name}\n Health: {enemy.health}\n Atk: {enemy.attack} | Def: {enemy.defense} | Spd: {enemy.speed}\n--------------------------\n{player.name}\n Health: {player.health}\n Atk: {player.attack} | Def: {player.defense} | Spd: {player.speed}"
            )

            if (
                enemy.health <= 0
            ):  # checks if enemy is dead and breaks out of while loop if it is
                print(
                    f"{enemy.name} killed."
                )  # need to add experience gained based on the enemy, possibly base it off of the difficulty
                player.exp += 1
                input("Press enter to proceed.")
                del enemy
                break

            print()
            player.print_skill_options()
            input("Enter your choice: ")
            self.print_line()
            enemy.health -= 5

        self.turns_since_last_encounter = 0


# ---functions
def intro_to_game() -> None:  # introduces the game and asks for the user's name/class/stats
    print(
        "Welcome to Text Based RPG!\n*Work in progress, currently best played in terminal"
    )
    print()


def create_player():
    char: str = ""
    name: str = ""

    print("Choose your class!")
    print("'K' for Knight | 'T' for Thief | 'V' for Vampire")

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

    print("----------------------------")
    print(f"You chose {char}!")

    while True:
        name = input("What is your name: ")
        if name == "":
            print("Please enter a name!")
        else:
            break

    print("----------------------------")
    print(f"So your name is {name} and you are a {char}!")

    input("Press enter to proceed to the Map!")

    if char == "Knight":
        return Knight(name, 10, 5, 5, 5, 20, 20, [])
    elif char == "Thief":
        return Thief(name, 10, 5, 5, 5, 20, 20, [])
    elif char == "Vampire":
        return Vampire(name, 10, 5, 5, 5, 20, 20, [])
    else:
        print("There is an error")


def create_enemy(map) -> Enemy:
    # Tier system
    # A tier
    # B tier
    # C tier
    return Enemy("Rat", 15, 5, 5, 5)


def ask_for_action():  # character movement etc
    print("What would you like to do?")


# ---main
if __name__ == "__main__":

    intro_to_game()
    player = create_player()
    map = Map()
    event = EventManager()

    while True:
        event.clear_terminal()  # change to 'clear' for MacOS machines
        map.print_visible_area(player)
        event.print_line()
        player.move(map)
        event.print_line()
        if event.check_for_encounter(player, map):
            event.initiate_encounter(player, map)
            event.print_line()
        if player.check_for_level_up():
            player.level_up()
            event.print_line()

        event.complete_turn()  # still need to write the code that resets the turns since encounter in the event manager object

    #   if event.check_for_encounter(player, map):
#       pass
#         if check_levelup():
#         player.levelup()


# game engine

# while True:


# Testing
# player = Knight("Josh", 50, 10, 5, 10, 10, [])
# player.showCurrentStats()
# player.powerAttack()
