def summation(numbers: list[int]) -> int:
    """
    Returns the sum of all integers in the list.
    """
    total = 0  # Start with zero
    for num in numbers:  # Go through each number
        total += num  # Add it to the total
    return total  # Return the final sum

def find_negative(numbers: list[int]) -> int:
    """
    Returns the index of the single negative number in the list.
    """
    for i in range(len(numbers)):  # Loop using index
        if numbers[i] < 0:  # Check if it's negative
            return i  # Return the index if found
    return -1  # If no negative found (shouldn't happen)

def find_greatest(numbers: list[int]) -> int:
    """
    Returns the largest integer in the list.
    """
    if not numbers:  # Handle empty list
        return None
    greatest = numbers[0]  # Start with the first number
    for num in numbers:  # Check each number
        if num > greatest:  # If it's bigger
            greatest = num  # Update greatest
    return greatest  # Return the biggest one

def remove(numbers: list[int], n: int) -> list[int]:
    """
    Returns a new list with all instances of n removed.
    """
    result = []  # Start with an empty list
    for num in numbers:  # Check each number
        if num != n:  # If it's not the one to remove
            result.append(num)  # Keep it
    return result  # Return the filtered list

def round_up(floats: list[float]) -> list[int]:
    """
    Rounds each float up if its decimal is >= 0.5, otherwise rounds down.
    """
    result = []  # Start with an empty list
    for f in floats:  # Go through each float
        if f - int(f) >= 0.5:  # Check decimal part
            result.append(int(f + 0.5))  # Round up
        else:
            result.append(int(f))  # Round down
    return result  # Return rounded list

def evens_only(numbers: list[int]) -> list[int]:
    """
    Returns a list of only the even numbers from the original list.
    """
    result = []  # Start with an empty list
    for num in numbers:  # Check each number
        if num % 2 == 0:  # If it's even
            result.append(num)  # Keep it
    return result  # Return evens only

def last_of_four_digits(numbers: list[int]) -> list[int]:
    """
    Returns a list of the last digit from each four-digit number.
    """
    result = []  # Start with an empty list
    for num in numbers:  # Go through each number
        result.append(num % 10)  # Get last digit
    return result  # Return the list of digits

def merge(first: list[int], second: list[int]) -> list[int]:
    """
    Merges two sorted lists and returns a new sorted list.
    """
    combined = []  # Start with an empty list
    for num in first:  # Add all from first
        combined.append(num)
    for num in second:  # Add all from second
        combined.append(num)
    combined.sort()  # Sort the combined list
    return combined  # Return the sorted result
