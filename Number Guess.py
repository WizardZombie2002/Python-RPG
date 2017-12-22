import random
print("""Let's play a guessing game! Guess a number between 1 and 100.
Try to get it in 6 tries!""")
cr = [1,100]
tries = 1
while True:
    x = int(input('Guess?'))
    if x > cr[1]:
        print(str(x) + ' is too large!')
    elif x < cr[0]:
        print(str(x) + ' is too small!')
    elif x == cr[0] and x == cr[1]:
        print(str(x) + ' is correct!')
        break
    else:
        lower = [cr[0], x-1]
        higher = [x+1, cr[1]]
        l = lower[1]-lower[0]
        h = higher[1]-higher[0]
        if l>h:
            cr = lower
            print(str(x) + ' is too large!')
        elif h>l:
            cr = higher
            print(str(x) + ' is too small!')
        else:
            t = random.randint(1,2)
            if t == 1:
                cr = lower
                print(str(x) + ' is too large!')
            else:
                cr = higher
                print(str(x) + ' is too small!')
    tries += 1
print('You took '+str(tries)+" tries! That's too many!")
