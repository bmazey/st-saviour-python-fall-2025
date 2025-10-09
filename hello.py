import random
if __name__ == '__main__':

 print('Welcome to AP CS: Principles!')

letters = 'abcdefghijklmnopqrstuvwxyz'
print('the length of letters is: ' + str(len(letters))) 
r = random.randint(0, len(letters) - 1)
print('the random int is: ' + str(r))
print('the random letter is: ' + letters[r])

 # s = 'september'
 # c = s[1]
 # print(c) 
 


