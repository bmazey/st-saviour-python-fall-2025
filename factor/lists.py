
def summation(numbers: list[int]) -> int:
    """
    summation() accepts a list of integers and returns the sum 
    of all numbers within as an int.
        ex: [0, 2, -1, 15] -> 16
    """

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
   
    # TODO
    i = 0
    while i < len(numbers):
        # ensures that its only checking the numbers in the list
        if numbers[i] < 0:
            # negatives less than 0
            return i
        i+=1


def find_greatest(numbers: list[int]) -> int:
    """
    find_greatest() accepts a list of integers and returns the greatest number
    found within.
        ex: [11, 13, -1, 4, 9] -> 13
    """

    # TODO
    greatest = numbers[0]
    for number in numbers:
        if number > greatest:
            # if the number is greatest then the assumed greatest, it is by definition the greatest
            greatest = number

    return greatest

def remove(numbers: list[int], n: int) -> list[int]:
    """
    remove() accepts a list of integers and an int n. The function removes 
    *all instances* of n from the provided list and returns a new list.
        ex: [0, 1, 1, 2, 2, 3], n = 2 -> [0, 1, 1, 3]
    """

    # TODO
    result = []
    for number in numbers:
        if number !=n:
            result.append(number)
            # append adds something to the end of the list

    return result

def round_up(floats: list[float]) -> list[int]:
    """
    round_up() accepts a list of *non-negative* floats and returns a list of
    rounded integers. Floats are rounded up iff the decimal is >= 0.5.
        ex: [1.2, 3.5, 4.2, 0.0] -> [1, 4, 4, 0]
    """

    # TODO

    result = []
    # easier to create a new list than change everything in current list
    for num in floats:
        if num - int(num) >= 0.5:
            # part of the last lab
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

    # TODO
    result = []
    i = 0
    # make sure to initialize i before using it
    while i < len(numbers):
        if numbers[i] % 2 == 0:
            result.append(numbers[i])
        i+=1
    # i+=1 needs to be indented to line up with the if

    return result

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    last_of_four_digits() accepts a list of four-digit integers and returns a new
    list containing only the last digit of each number in the original sequence.
        ex: [1004, 1112, 5667, 8009] -> [4, 2, 7, 9]
    """

    # TODO

    return [n % 10 for n in numbers]
# modulo 10 just returns the last number, like 1004/10 = 100 R 4, so it prints just the rekainder for n in numbers

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    merge() accepts two *pre-sorted* lists of integers and returns 
    a new *sorted* list. WARNING do not assume lists are of equal length!
    You may only use the built-in list.sort() function to assist.
        ex: [0, 2, 4, 8] + [1, 3, 5] -> [0, 1, 2, 3, 4, 5, 8]
    """

    # TODO +5 Bonus

    merged_list = first + second
    # combines the two lists, first and second
    merged_list.sort()
    # built in function that sorts lists
    return merged_list
