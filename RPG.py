#Made by Tinsel Ninja AKA WizardZombie
#Fully commented so you can edit it
#Let's begin

#Import random library
from random import *

#set variables
inventory = []
health = 100
defense = 0
battle_key = 0

#Define the consumable items system
def useConsumable():
    health = health + (randint(20, 50))

#Define the help menu
def showInstructions():
    print('RPG Game')
    print('========')
    print('Commands:')
    print('attack [enemy]')
    print('use [consumable item]')
    print('go [direction]')
    print('get [item]')

#Define the player information
def showStatus():
    print('================')
    print('You are in the ' +rooms[currentRoom]['name'])
    print('Health: ')
    print(health)
    print('Inventory : ' +str(inventory))
    #Check if there is an 'item' in the room
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print('================')
    #Check if there is a 'consumable' in the room
    if 'consumable' in rooms[currentRoom]:
        print('You see a ' +rooms[currentRoom]['consumable'])
        print('================')
    #Check if there is an 'enemy' in the room
    if 'enemy' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['enemy'])
    if 'armour_cheatplate' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['armour_chestplate'] + ' Chestplate!')
    print('================')

#Define the attack system
def attackMonster():
    global health
    global battle_key
    global inventory
    print('Attack the monster!')
    attack_key = input('Type strike to attack!')
    if attack_key == 'strike':
        battle_key = (randint(0, 10))
    if battle_key >= 5:
        print('The monster has been slain!')
    elif battle_key < 5:
        print('The monster attacks! You take damage!')
        print('Health: ')
        print(health)
        health = health - (randint(5, 10))
        attackMonster()
    else:
        print('')
        attackMonster()

#The rooms are stored as a dictionary
rooms = {
#The Grand Hall is the room you start in
    1 : { 'name' : 'Grand Hall',
          'right' : 2,
          'back' : 3,
          'left' : 4,
          'forward' : 6 },
    2 : { 'name' : 'Master Bedroom',
          'left' : 1,
          'back' : 4,
          'item' : 'grasscutter',
          'item' : 'ebon chesplate'},

    3 : { 'name' : 'Main Kitchen',
          'right' : 4,
          'forward' : 1,
          'enemy' : 'waiyida'},

    4 : { 'name' : ' Bathroom',
          'up' : 5},

    5 : { 'name' : 'Attic',
          'down' : 4,
          'enemy' : 'fieryspite',
          'item' : 'deathbrand'},

    6 : { 'name' : 'Staircase To First Floor',
          'up' : 8,
          'down' : 7,
          'back' : 1,
          'enemy' : 'fieryspite' },

    7 : { 'name' : 'Basement',
          'up' : 6,
          'item' : 'ironbark',
          'enemy' : 'crysos' },

    8 : { 'name' : 'Upstairs Hall',
          'forward' : 9,
          'back' : 11,
          'right' : 12,
          'left' : 10,
          'down' : 6,
          'enemy' : 'waiyida',
          'item' : 'battlescythe' },

    9 : { 'name' : 'other Bathroom',
          'enemy' : 'fieryspite',
          'item' : 'potion',
          'backward' : 8 },

    10 : { 'name' : 'Spare Room',
          'right' : 8 },

    11 : { 'name' : 'Guest Bedroom',
          'forward' : 8 },

    12 : { 'name' : 'Office',
           'left' : 8 },

    
    }
#Set the start room. To change, pick from dictionary number.
currentRoom = 1
#Show instructions
showInstructions()
#Loop infinitely
while True:
    #always show player info
    showStatus()

    move = input('>').lower().split()
    #The 'go' mechanic in the game
    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way")

    #The 'get mechanic in the game
    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #Add the item to your inventory
            inventory += [move[1]]
            print(move[1] + ' got!')
            #Delete the item from the room so you can't pick it up again
            del rooms[currentRoom]['item']
        else:
            print("Can't get " +move[1] + "!")

    #The 'attack' mechanic in the game
    if move[0] == 'attack':
        if 'enemy' in rooms[currentRoom] and move[1] in rooms[currentRoom]['enemy']:
            #Run the attack function, attackMonster
            attackMonster()
            print(move[1] + ' killed!')
            print('Health: ')
            print(health)
            #Delete the enemy from the room so it doesn't appear again 
            del rooms[currentRoom]['enemy']
        else:
            print("Can't see " +move[1] + "!")

