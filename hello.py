
# if __name__ == '__main__':
#     print('Welcome to AP CS: Principles!')


# words  = ['the', 'quick', 'brown', 'fox']
# words.append('jumps')
# words.append('over')
# words.append('the')
# words.append('lazy')
# words.append('dog')

# result = []
# for word in words: 
#     if word != 'the':# this if statement belongs the one above it
#         result.append(word)#this is what should happen if the above if statement is true.

#         for entry in result: 
#             print(entry)

#Remove
# word = 'racecar'
# reverse = ''

# i = len(word) -1 
# while i >= 0:
#     reverse += word[i]
#     i -= 1

# if word == reverse:
#     print(word + ' is a palindrome!')
# else: 
#     print(word + ' is NOT a palindrome!') 

# THIS IS THE HARD WAY THE NEXT IS THE SIMPLE WAY

word = 'racecar'
reverse = ''

if word == word[::-1]:
    print(word + ' is a palindrome!')
else: 
    print(word + ' is NOT a palindrome!') 