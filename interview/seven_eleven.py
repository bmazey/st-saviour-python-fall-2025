
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """
    # use the modulo to show if the number is a multiple  of 7 and 11
    # a modulo is used to show the remainder
    if number % 7 == 0 and number % 11 == 0:
        return 'seveneleven'
    # use the modulo to show if the number is just a multiple of 7 only
    if number % 7 == 0: 
        return 'seven'
    # use the modulo to show if the number is just a multiple of 11 only
    if number % 11 == 0:
        return 'eleven'
    # return an empty string to show if its not a multiple of either 7 or 11
    return ''  
