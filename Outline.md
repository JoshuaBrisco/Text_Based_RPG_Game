
Text Based RPG Game

Systems:
  Game engine:
    While true loop which only ends when the game is complete or a specific imput is entered
    Likely sorted into phases
      1) Begin phase OR possibly accessible at any time (inventory management, consumables)
      2) Movement
      3) Encounter chance (Combat will loop until complete, then give exp)
      4) checkLevelUp
      5) counter turnsComplete += 1
  Combat:
    Damge rolls
      Option A: Range of possible numbers
      Option B: Dice based
  Map:
    A list of lists/array depending on what is possible with python
    Implementation of vision range?
    Big map using letters to identify what type of terrain it is (F = forrest, M/A = mountain, etc), thinking 100 x 100
    Only see ~8x8 while moving around with imputting WASD
  Leveling:
    Stat increases
    Stats that could work
      Attack or might: works hand in hand with defense
      Magic or might: affects spellcasters damage, healing of the paladins heal, may ignore some defense
      Defense: uses a formula to determine how much reduction in damage
      Health: increases damage capable of taking
      Speed: going first/evasion
      ? More
    Possible specializations (Knight/Paladin/Death Knight OR Thief/Assassin/Shadow OR Vampire/Werewolf)
    Skill learning (possibly specializations)
      Power abilities
        Knight: an attack that does 1.5x damage/stuns
        Thief:
        Vampire:
      Special abilities
        Knight: a heal
        Thief: 
        Vampire: an ability that damages the enemy and heals the character
      Passives:
        Knight:
        Thief: 
        Vampire:
      Movement ability per class
        Knight:
        Assassin: an ability to reduce encounter chance to 0% for some turns
        Vampire:
      Ultimates?
  Enemy randomization
    Archetypes that may have slight variations and different movesets
  Encounter chance calulation
    Likely will increase exponentially with a cap (start at 0%->1%->2%->4%->8%, end at 32%) depending on the tile the character is on


To do:
Design game "engine"
  Explore mode
    Player movement arround an array type map
  Combat mode
    Combat will occur occastionally, a chance based encounter based on the tile that they are on
    Will loop each char turns in the fight's turns until health <= 0
  All modes
    Certain functions will need to be available no matter what mode we are in, they
    will be called with a text "letter", to be determined ("i" for inventory)
Design how combat will function
  Math and interaction between attack/defense
  May add additional stats(speed, magic) for additional class distinction