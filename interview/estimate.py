def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # Check if the decimal is >= 0.5
    if number - int(number) >= 0.5:  # Subtract integer from number
        return int(number) + 1  # If >=0.5, add 1 to round up
    # If <0.5
    return int(number)  # Return number without decimal