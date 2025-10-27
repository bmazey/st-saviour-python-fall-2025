if __name__ == '__main__':
    # Hi from Jordan 
    print('Welcome to AP CS: Principles!')

word = 'october'
reverse = ''

for c in word:
    reverse = c + reverse

if word == reverse:
    print(word + ' is a palindrome')
else:
    print(word + ' is NOT a palindrome')

# i = len(word) - 1 
# white i >= 0