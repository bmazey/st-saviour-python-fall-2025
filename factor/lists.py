
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """
    # uses a for loop to add each successive number to the original number of 0
    # result now represents the final sum of all the numbers in the list
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
    
    # indexing is used to access the position of the numbers 
    # conditions of the while loop allow for all numbers in the list to testing against being less than zeer
    # returning 0 after indexing returns the position of the number that was less than 0
    i = 0
    while i < len(numbers):
        if numbers[i] < 0:
            return i
        i += 1

    return 0

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    # start with position of first number 
    # use a for loop to explain that each successive number is greater than the number before it
    # greatest = number means that the value of the number being tested is assigned to greatest
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            greatest = number

    return greatest

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    # use empty list, iteration, and a for loop to remove a specific integer
    # after removing the specific integer use the append function to create the new list 
    result = []
    for number in numbers: 
        if number != n: 
            result.append(number)


    return result

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    # starts with an empty list 
    # seperating the decimal from the integer while in the loop tests whether the number will be rounded up or down
    # the conditions and the append function create a new list that has the original numbers rounded properly
    result = []
    for num in floats:
        if num - int(num) >= 0.5:
            result.append(int(num) + 1)
        else:
            result.append(int(num))
    return result

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """

    # indexing allows each position in the list to be checked against the conditions in the loop
    # each number in the list is checked to see if when divided by two it produces no remainder
    # the append function is used to create a new list of numbers that satisfy the conditions
    result = []
    i = 0
    while i < len(numbers):
        if numbers[i] % 2 == 0:  
            result.append(numbers[i])
        i += 1

    return result 

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # returning the outcome of a for loop that tests each number in the list to see the remainder when divided by ten
    return [n % 10 for n in numbers]

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """
    
    # uses the list.sort function to comment the first and second lists
    # the merged list returned
    merge_list = first + second
    merge_list.sort()
    return merge_list

