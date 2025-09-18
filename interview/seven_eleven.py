
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    if number % 7 == 0 and number % 11 == 0:#use modulo to show if the number is a multiple  of 7 and 11
        return 'seveneleven'
    if number % 7 == 0: # use the modulo to show if the number is just a multiple of 7 only.
        return 'seven'
    if number % 11 == 0:# use the modulo to show if the number is just a multiple of 11 only.
        return 'eleven'
    return ''   # return an empty string to show if its not a multiple of either 7 or 11. 