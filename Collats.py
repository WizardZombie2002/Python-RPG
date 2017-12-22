def collatz(i):
    if i % 2 == 0:   #If i is divisible by 2, divide it by 2
        i //= 2
    else:    #If not, multiply by 3 and add 1
        i *= 3
        i += 1
    return i
     
def run(i):
    while i != 1:   #Keep going until i=1
        if i == int(i):   #If i is an integer, take away the decimal point
            i = int(i)
        print(i,end="\t")   #Tell the user the new number
        i = collatz(i)   #Collatz i
    print(1)   #After the program is done, print 1 because it didn't print earlier
     
x = float(input("Give me a number: "))   #Get the user's number as a decimal
run(x)   #Run the program on the user's number
