def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """
        # Check if number is a multiple of both 7 and 11 first 
    if number % 7 == 0 and number % 11 == 0:
        return 'seveneleven'
    # Check if number is only a multiple of 7.
    elif number % 7 == 0:
        return 'seven'
    # Check if number is only a multiple of 11.
    elif number % 11 == 0:
        return 'eleven'
    # Return empty string if none of the above conditions are met.
    else:
        return ''
