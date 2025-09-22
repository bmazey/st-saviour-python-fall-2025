import random

if __name__ == '__main__':
    #print('Welcome to AP CS: Principles!')
    
    letters = 'abcdefghijklmnopqrstuvwzyz'
    r = random.randint(0, len(letters) - 1)
    print('the random number is: ' + letters[r])
