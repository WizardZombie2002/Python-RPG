import random 
correctPassword = 'Hexagon?909'
guesses = 0
guess = ''

def changeme( brute_force ):
    correctPassword = str(random.randint(0,9999))
    Trial = ' '
    while Trial != correctPassword:
        Trial = str(random.randint(0,9999))
        print(Trial)
        if Trial == correctPassword:
            print('The password is: '+correctPassword)
            input()


while guess != correctPassword:
    guess = input('Try to guess the correct password: ')
    guesses = guesses + 1
    changeme( brute_force );

print('Password guessed correctly')

if guesses == 1:
    print('That took you 1 guess.')
else:
    print('That took you ' + str(guesses) + ' goes.')


