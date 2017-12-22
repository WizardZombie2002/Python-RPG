from random import *

inventory = []
health = 100
defense = 0
battle_key = 0

def useConsumable():
    health = health + (randint(20, 50))

def showInstructions():
    print('RPG Game')
    print('========')
    print('Commands:')
    print('attack [enemy]')
    print('use [consumable item]')
    print('go [direction]')
    print('get [item]')

def showStatus():
    print('================')
    print('You are in the ' +rooms[currentRoom]['name'])
    print('Health: ')
    print(health)
    print('Inventory : ' +str(inventory))
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print('================')
    if 'consumable' in rooms[currentRoom]:
        print('You see a ' +rooms[currentRoom]['consumable'])
        print('================')
    if 'enemy' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['enemy'])
    print('================')

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


rooms = {

    1 : { 'name' : 'Grand Hall',
          'east' : 2,
          'south' : 3,
          'west' : 4,
          'north' : 6 },
    
    2 : { 'name' : 'Master Bedroom',
          'west' : 1,
          'south' : 4,
          'item' : 'grasscutter',
          'item' : 'chestplate'},

    3 : { 'name' : 'Main Kitchen',
          'east' : 4,
          'north' : 1,
          'enemy' : 'waiyida'},

    4 : { 'name' : ' Bathroom',
          'up' : 5},

    5 : { 'name' : 'Attic',
          'down' : 3,
          'enemy' : 'fieryspite',
          'item' : 'deathbrand'},

    6 : { 'name' : 'Staircase To First Floor',
          'up' : 8,
          'down' : 7,
          'south' : 1,
          'enemy' : 'fieryspite' },

    7 : { 'name' : 'Basement',
          'up' : 6,
          'item' : 'ironbark',
          'enemy' : 'crysos' },

    8 : { 'name' : 'Upstairs Hall',
          'north' : 9,
          'south' : 11,
          'east' : 12,
          'west' : 10,
          'down' : 6,
          'enemy' : 'waiyida',
          'item' : 'battlescythe' },

    9 : { 'name' : 'other Bathroom',
          'enemy' : 'fieryspite',
          'consumable' : 'potion',
          'south' : 8 },

    10 : { 'name' : 'Spare Room',
          'east' : 8 },

    11 : { 'name' : 'Guest Bedroom',
          'north' : 8 },

    12 : { 'name' : 'Office',
           'west' : 8 },

    
    }

currentRoom = 1

showInstructions()

while True:

    showStatus()

    move = input('>').lower().split()

    if move[0] == 'go':
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way")

    if move[0] == 'get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
           inventory += [move[1]]
           print(move[1] + ' got!')
           del rooms[currentRoom]['item']
        else:
            print("Can't get " +move[1] + "!")

    if move[0] == 'attack':
        if 'enemy' in rooms[currentRoom] and move[1] in rooms[currentRoom]['enemy']:
            attackMonster()
            print(move[1] + ' killed!')
            print('Health: ')
            print(health)
            del rooms[currentRoom]['enemy']
        else:
            print("Can't see " +move[1] + "!")

    if move[0] == 'use':
        if 'consumable' in rooms[currentRoom] and move[1] in rooms[currentRoom]['enemy']:
            useConsumable()
            print(move[1] + ' used!')
            print('Health: ')
            print(health)
            del rooms[currentRoom]['consumable']
        else:
            print("Can't see " +move[1] + "!")
