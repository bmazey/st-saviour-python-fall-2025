
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """
    #ADD COMMENTS: DONE
    result = 0 # tells you where to start
    for number in numbers: # to show hat the number that comes out of numbers will be added onto next
        result += number  # shows that the number will be  added on to 
      
    return result

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """
    index = 0  # starts at position zero
    while index < len(numbers): # the loop will keep going as long as the index is less than the len of the numbers
        if numbers[index] < 0: # shows that if the index is less than 0 
            return index # it will return the the index
        index += 1

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """
    greatest = numbers[0] # starts to check the numbers starting with the index zero. 
    for number in numbers: # checks all the numbers in the list
        if number > greatest: # will check to see if the number is larger than the greatest number
            greatest = number # will see if the greatest number is the same as the number given
    
    return  greatest # will return the greatest number

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """
    result = [] # will give an empty list
    for number in numbers: # will go through all the numbers
        if number != n: # makes sure the numbers do not = n
            result.append(number) # adds the numbers when they do not = to n to the result list. 

    return result # this returns the list

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """
    result = [] # this gives an empty list
    for number in floats: # evaluates the numbers in the list of decimal and whole numbers
        decimal = number % 1 # shows if the decimal is equal to the mod 1 of the number 
        if decimal >= 0.5: # shows if the decimal is greater than 0.5 
            result.append(int(number) + 1) # if that is true than add 1 to the whole number of that number
        else: 
            result.append(int(number)) # if the decimal is lower than 0.5 than you will return only the integer 

    return result # will return the result

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """
    result = [] # starts off with an empty list
    for num in numbers: # evaluates the numbers
        if num % 2 == 0: # this says if when doing % 2 the number equals 0 then 
            result.append(num) # you can add it to the final result only if it was equal to 0
    
    return result # this returns the list

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    last_digits = [] # shows an empty list of numbers
    for number in numbers: # check the entire list of numbers
        last_digits.append(number % 10) # using % 10 will allow you to always return the last value of a 4 digit number
        
    return last_digits # this returns the output 

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """
    new_list = first + second # this states that the new list being returned with the two lists merged. 
    new_list.sort(first + second) # this adds the two lists together

    return new_list # returns the new list
