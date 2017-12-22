def bpm():
    bpm = int(input('ENTER AGE >>>  '))
    bpm2 = str(220 - bpm)
    print('Your BPM should be ' + bpm2)

def calc():
    print('                              CHOOSE CALCULATION')
    print('                                      +')
    print('                                      -')
    print('                                      *')
    print('                                      /')
    print('                                     BACK')
    calculation = str(input('>>>  '))
    
    if calculation == 'BACK':
        menu()
        
    if calculation == '+':
        first_num = int(input('FIRST NUMBER >>>  '))
        second_num = int(input('SECOND NUMBER >>> '))
        print(first_num + second_num)
        calc()

    if calculation == '-':
        third_num = int(input('FIRST NUMBER >>>  '))
        fourth_num = int(input('SECOND NUMBER >>> '))
        print(third_num - fourth_num)
        calc()

    if calculation == '*':
        fifth_num = int(input('FIRST NUMBER >>>  '))
        sixth_num = int(input('SECOND NUMBER >>> '))
        print(fifth_num * sixth_num)
        calc()

    if calculation == '/':
        seventh_num = int(input('FIRST NUMBER >>>  '))
        eighth_num = int(input('SECOND NUMBER >>> '))
        print(seventh_num / eighth_num)
        calc()

    if calculation == 'BACK':
        menu()
        
def menu():
    print('                                  MAIN MENU')
    print('                            CHOOSE AREA TO ACCESS')
    print('                                    .calc')
    print('                                     .bpm')
    print('                                     .txt')
    choice = str(input('>>>  '))
    if choice == '.calc':
        calc()
    elif choice == '.bpm':
        bpm()
    elif choice == '':

def password_system():
    password = str(input('Please enter password to continue >>>  '))
    if password == 'Hexagon?909':
        print('Access Granted')
        print('')
        menu()
    else:
        print ('Access Denied')
        password_system()

password_system()
