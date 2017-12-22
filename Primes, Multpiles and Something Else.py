# Is_Prime
# by CaptainFlint
     
def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True if is x is a multiple of y,
    False if otherwise'''
    # check if y divides evenly into x
    return (x % y == 0)
     
def is_prime(n):
    '''is_prime(n) -> bool
    returns True if n is prime, False if n is not prime'''
    isPrime = True  # initialize the isPrime variable
    # check every divisor from 2 up to sqrt(n)
    for div in range(2,int(n**0.5)+1):
        if is_multiple(n,div):
            isPrime = False  # n isn't prime!
    return isPrime
     
def list_of_primes(first,second):
    '''is_prime(n) -> str
    makes a list of primes from first to second, inclusive'''
    listOfPrimes = list()
    if first <= 1:
        first = input('Please enter an integer *greater than* 1: ')
        while first.isdigit() is False:
            first = input('Please enter an integer *greater than* 1: ')
        first = int(first)
    for x in range(first,int(second)+1):
        if is_prime(x) is True: # if the number is prime
            listOfPrimes.append(x)
    return listOfPrimes
