def summation(numbers: list[int]) -> int:
    """
    Returns the sum of all integers in the list.
    """
    return sum(numbers)  # Built-in sum function adds all elements

def find_negative(numbers: list[int]) -> int:
    """
    Returns the index of the single negative number in the list.
    """
    for i, num in enumerate(numbers):  # Loop through with index
        if num < 0:
            return i  # Return index when negative is found
    return -1  # Fallback (shouldn't happen with valid input)

def find_greatest(numbers: list[int]) -> int:
    """
    Returns the largest integer in the list.
    """
    return max(numbers)  # Built-in max function finds the greatest value

def remove(numbers: list[int], n: int) -> list[int]:
    """
    Returns a new list with all instances of n removed.
    """
    return [num for num in numbers if num != n]  # List comprehension filters out n

def round_up(floats: list[float]) -> list[int]:
    """
    Rounds each float up if its decimal is >= 0.5, otherwise rounds down.
    """
    return [int(f + 0.5) if f - int(f) >= 0.5 else int(f) for f in floats]
    # Adds 0.5 and converts to int if decimal >= 0.5

def evens_only(numbers: list[int]) -> list[int]:
    """
    Returns a list of only the even numbers from the original list.
    """
    return [num for num in numbers if num % 2 == 0]  # Keep numbers divisible by 2

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    Returns a list of the last digit from each four-digit number.
    """
    return [num % 10 for num in numbers]  # Modulo 10 gives the last digit

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    Merges two sorted lists and returns a new sorted list.
    """
    combined = first + second  # Combine both lists
    combined.sort()  # Sort the combined list
    return combined