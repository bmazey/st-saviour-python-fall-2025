
def rounder(number: float) -> int:
    """
    round accepts a float and returns a rounded integer.
    the number is rounded up iff the decimal is >= .5
    """
    
    decimal = number - int(number)

    if decimal >= 0.5: 
        result = int(number) + 1 # add 1 to round up decimal because the decimal is greater than .5
    else:
        result = int(number) 

    return result

  
