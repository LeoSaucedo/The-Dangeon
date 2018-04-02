from time import sleep
from random import randint

##Global variables
weaponStrength = 0
weaponName = None
userChoice = 0
userHp = 250
userXp = 0
userStrength = 100
enemyHealth = 0


##Functions
#Function that asks for a choice, to be used in a non-battle situation.
def promptChoice():
  global userChoice, userHp
  print("--Your HP is %s." % (userHp))
  print("--Your XP is %s." % (userXp))
  userChoice = raw_input("What do you do? -->")
  if userChoice != "1" and userChoice !="2":
    print("You selected an invalid choice!")
    promptChoice()

#Function that asks for a choice, to be used in a battle situation.
def promptAttackChoice():
  global userChoice, userHp, enemyHp
  print("--Your HP is %s." % (userHp))
  print("--Enemy's HP is %s." % (enemyHealth))
  userChoice = raw_input("What do you do? -->")

#Game over screen.
def gameOver():
  print('''
   _____          __  __ ______    ______      ________ _____  
  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ 
 | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |
 | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / 
 | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ 
  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\
                                                               
  ''')
  exit()
def victory():
  print('''
 __     ______  _    _  __          _______ _   _ _ 
 \ \   / / __ \| |  | | \ \        / /_   _| \ | | |
  \ \_/ / |  | | |  | |  \ \  /\  / /  | | |  \| | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_(_)
Thanks for playing!
  ''')
  exit()

#Functions that print a line of characters dividing the different modes of the game.
def levelDivider():
  print("----------------------------------")
def battleDivider():
  print("++++++++++++++++++++++++++++++++++")

#Function that displays the intro ASCII art, as well as the intro scenario.
def introText():
  print('''
.___________. __    __   _______     _______       ___      .__   __.   _______  _______   ______   .__   __.
|           ||  |  |  | |   ____|   |       \     /   \     |  \ |  |  /  _____||   ____| /  __  \  |  \ |  |
`---|  |----`|  |__|  | |  |__      |  .--.  |   /  ^  \    |   \|  | |  |  __  |  |__   |  |  |  | |   \|  |
    |  |     |   __   | |   __|     |  |  |  |  /  /_\  \   |  . `  | |  | |_ | |   __|  |  |  |  | |  . `  |
    |  |     |  |  |  | |  |____    |  '--'  | /  _____  \  |  |\   | |  |__| | |  |____ |  `--'  | |  |\   |
    |__|     |__|  |__| |_______|   |_______/ /__/     \__\ |__| \__|  \______| |_______| \______/  |__| \__|
  ''')
  sleep(2)
  print("Press Enter to continue...")
  raw_input()
  print("GASP! You awake in a dungeon.")
  sleep(1)
  print("You hear the growls of threatening monsters out in the distance.")
  sleep(1)

#Function that selects random characters from a set of enemies and puts them into the battle function.
def randomBattle():
  enemyID = randint(1,3)
  if enemyID == 1:
    enemyName = "Andrew"
    enemyStrength = 100
    enemyHp = 100
    enemyXp = 1
  elif enemyID == 2:
    enemyName = "Luke"
    enemyStrength = 150
    enemyHp = 150
    enemyXp = 5
  elif enemyID == 3:
   enemyName = "Tom"
   enemyStrength = 200
   enemyHp = 300
   enemyXp = 10
  battle(enemyName, enemyStrength, enemyHp, enemyXp)

#Function that is used for every battle.
def battle(enemyName, enemyStrength, enemyHp, enemyXp):
  global enemyHealth, userHp, userXp
  enemyHealth = enemyHp
  print("Suddenly, a wild %s appears!" % (enemyName))
  print("(1)Attack!\n(2)Flee")
  promptChoice()
  while userHp >0 and enemyHp >0 and userChoice == "1":
    battleDivider()
    if userHp >0 and enemyHp > 0:
      print("(1)Attack %s.\n(2)Flee." % (enemyName))
      promptAttackChoice()
    if userChoice == "1":
      userAttackStrength = ((randint(userStrength, (userStrength + (userStrength/10))) * weaponStrength) + userXp)
      enemyHp = enemyHp - userAttackStrength
      print("You attack! %s damage!" % (userAttackStrength))
      sleep(2)
      enemyAttackStrength = (randint(0,enemyStrength))
      userHp = userHp - enemyAttackStrength
      print("Enemy attacks! %s damage!" % (enemyAttackStrength))
      enemyHealth = enemyHp
      sleep(1)
    if userHp <= 0:
      gameOver()
    elif enemyHp <= 0:
      userXp = userXp + enemyXp
      print("Victory! XP + %s." % (enemyXp))
      battleDivider()
      raw_input("Press ENTER to continue...")

#Function used when the user is given the option to pick up a weapon.
def swordPickup(weaponName, weaponValue):
  promptChoice()
  if userChoice == "1":
    print("You pick up the %s sword!" % (weaponName))
    print("Strength multiplier stat +%s" % (weaponValue))
    global weaponStrength
    weaponStrength = weaponValue
  else:
    print("You must pick up the weapon!\nYou're gonna fight, duh")
    swordPickup(weaponName, weaponValue)

#Function that randomly picks whether player gets an HP boost or not.
def exploreChoice():
  print("There are things scattered around the dungeon.\n(1)Explore.\n(2)I don't need to explore!")
  promptChoice()
  if userChoice == "1":
    jackpotChance = randint(0, 1)
    if jackpotChance == 1:
      candyStrength = randint(25, 150)
      global userHp
      userHp = userHp + candyStrength
      print("You find a piece of candy! HP + %s" % (candyStrength))
    elif jackpotChance == 0:
      print("You find nothing!")
      
#Function that keeps monsters coming to the user until a certain XP.
def battleGrind(targetXP):
  while userXp < targetXP:
    levelDivider()
    exploreChoice()
    levelDivider()
    randomBattle()

##Game Code
#Runs the introduction screen text.
introText()

#Wooden Sword Pickup
print("Next to you, you see a stubby wooden sword.")
sleep(1)
print("(1)Pick up the sword.\n(2)Leave it be.")
swordPickup("Wooden", 1)

#Battle levels (XP has to reach 20 in order for the boss battle option to trigger)
battleGrind(19)

#Diamond Sword Pickup
print("Upon defeating the last monster, you find a Diamond sword!")
sleep(1)
print("(1)Pick up the sword.\n(2)Leave it be.")
swordPickup("Diamond", 5)
levelDivider()
print("On the sword, you see a note.")
sleep(2)
print("It reads:")
sleep(1)
print("Come to the pit, when you're ready.")
sleep(2)
print("You can see the pit, it's not too far off into the distance.")
sleep(1)
print("After an hour of traveling towards it, you get tired and decide to take a break.")
exploreChoice()
print("You see a flash!")
levelDivider()
print("~~~~BOSS BATTLE~~~~")
levelDivider()
battle("Danny", 1000, 1000, 1000)
if userXp > 500:
  victory()
else:
  gameOver()


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  