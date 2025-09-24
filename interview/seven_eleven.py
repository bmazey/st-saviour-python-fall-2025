def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # Check if number is a multiple of both 7 and 11
    if number % 7 == 0 and number % 11 == 0:  # Check using modulo
        return 'seveneleven'  # Return string if both are true
    # Check if number is a multiple of 7
    elif number % 7 == 0:  # Check using modulo
        return 'seven'  # Return string if true
    # Check if number is a multiple of 11
    elif number % 11 == 0: # Check using modulo
        return 'eleven'  # Return string if true
    #If all of the above are false
    else:  # Take number if not a multiple of 7 or 11
        return ''  # Return empty string