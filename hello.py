
if __name__ == '__main__':
    # Hi from Jada
    # starting lab 2
    print('Welcome to AP CS: Principles!')

    numbers = [3, 14, 7, 88, 7]
    i = 0
    while i < len(numbers):
        print('index: ' + str(i) + ' content: ' + str(numbers[i]))
        i += 1

    numbers = [3, 14, 7, 88, 7, 11]
    for x in numbers:
        print(x)


    word = 'october'
    reverse = ''

    
       

    # for c in word:
        # reverse = c + reverse
    
    if word == word[::-1]:
        print(word +  'is a palindrome!')    
    else:
        print(word + ' is NOT a palindrome!')
   


