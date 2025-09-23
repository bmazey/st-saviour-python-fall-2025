import random
if __name__ == '__main__':
    print('Welcome to AP CS: Principles!')

# remember to import random so syntax error does not occur and the code can randomize a number
letters = 'abcdefghijklmnopqrstuvwxyz'
print('the length of letters is: ' + str(len(letters)))
r = random.randint(0, len(letters) - 1)
print('the random int is: ' + str(r))
print('the random letter is: ' + letters[r])

r = random.randint(0, len )


# s = 'september'
# c = s[1]
# print(c)

# x = 5
# y = 3
# print(x + y)