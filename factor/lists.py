
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

    # Stores the sum
    result = 0
    # Go through each number in the input
    for number in numbers:
        # Adds the current number to the result
        result += number
    # Returns the calculated sum
    return result

def find_negative(numbers: list[int]) -> int:
    """
    find_negative() accepts a list of integers containing one negative number
    and returns the *position* of the negative number. You may safely assume
    the provided list contains only a single negative number.
        ex: [11, 13, -1, 0, 9] -> 2
    """

    # Loop through list to find index and value
    for i, num in enumerate(numbers):
        # Checks if number is negative
        if num < 0:
            # Returns index of number if negative
            return i

def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    # Uses max function to find greatest number
    return max(numbers)

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    # Makes an empty list for the result
    result = []
    
    # Goes over each number in the list
    for number in numbers:
        # Checks if each number is not equal to n
        if number != n:
            # Adds the number to the new list
            result.append(number)
    
    # Returns the new list
    return result

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    # Rounds each float to the nearest int
    return [round(f) for f in floats]

def evens_only(numbers: list[int]) -> list[int]:
    """
    evens_only() accepts a list of integers and returns a new list containing
    only the even numbers found in the provided list, in their original order.
        ex: [3, 4, 7, 8, 12] -> [4, 8, 12]
    """

    # Returns a list of even numbers
    return [num for num in numbers if num % 2 == 0]

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # Modulo takes the last digit of each number
    return [num % 10 for num in numbers]

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

     # Creates an empty list for the result
    result = []
    i, j = 0, 0  # Indicates positions in the first and second lists
    
    # Compares both lists
    while i < len(first) and j < len(second):
        if first[i] < second[j]:
            # Attaches element in first list if it is smaller
            result.append(first[i])
            i += 1
        else:
            # Attaches element in the second list otherwises
            result.append(second[j])
            j += 1
    
    # Attaches any left over elements in the first list
    result.extend(first[i:])
    
    # Attaches any left over elements in the second list
    result.extend(second[j:])
    
    # Returns the combined, organized list
    return result