
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """

    # % is modulo which is the remainder
    decimal = number % 1 

    if decimal >= 0.5:
        # rounds up 
        return int(number) + 1
    #round down
    return int(number)
