import random

if __name__ == '__main__':
    # print('Welcome to AP CS: Principles!')

    # letters = 'abcdefghijklmnopqrstuvwxyz'
    # print('the length of letters is: ' + str(len(letters)))
    # r = random.randint(0, len(letters) - 1)
    # print('the random int is: ' + str(r))
    # print('the random letter is: ' + letters[r])

    # s = 'september'
    # c = s[1]
    # print(c)

    a = True
    b = False
    if a and not(b):
        print('go pandas')
    else:
        print('oops')


    # x = 5
    # y = 3
    # print(x + y)

    s = 'september'
    c = 'sept'
    c += 'ember'

    # this is a comment
    print('the address of s is: ' + str(id(s)))
    print('the address of c is: ' + str(id(c)))

    if s == c:
        print('the strings are the same')
    else:
        print('the strings are NOT the same')
