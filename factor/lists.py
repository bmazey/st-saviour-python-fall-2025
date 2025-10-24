
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """
    #ADD COMMENTS: DONE
    result = 0
    for number in numbers:
        result += number 
      
    return result

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """
    #USE A WHILE LOOP
    index = 0 
    while index < len(numbers):
        if numbers[index] < 0: 
            return index 
        index += 1

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """
    # Create a  variable greates then loop over all the numbers in the lsit and if that numbher is greater than yuou created than upsate it

    greatest = numbers[0]
    for number in numbers:
        if number > greatest: 
            greatest = number
    
    return  greatest
def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """
    result = []
    for number in numbers: 
        if number != n: # makes sure the numbers do not = n
            result.append(number) # adds the numbers not = to n to the result list. 

    return result

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """
    result = []
    for number in floats:
        decimal = number % 1
        if decimal >= 0.5:
            result.append(int(number) + 1)
        else: 
            result.append(int(number)) 

    return result 
def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """
# return new list of only even numbers --> % 2 = 0  ASK ASK ASK 
    result = []
    for num in numbers: 
        if num % 2 == 0:
            result.append(num)
    
    return result

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    last_digits = [] # shows an empty list of numbers
    for number in numbers:
        last_digits.append(number % 10) # using % 10 it will allow you to always return the last value of a 4 digit number
        
    return last_digits # this returns the output 

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    # TODO +5 Bonus

    return []
