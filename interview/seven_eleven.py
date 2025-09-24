
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    if number % 7 == 0 and number % 11 == 0: #returns seveneleven if number is a multiple of 7 and 11
        return 'seveneleven'
    if number % 7 == 0:  #returns seven if the number is a multiple of 7
        return 'seven'
    if number % 11 == 0:   #returns eleven if number is a multiple of 11
        return 'eleven'
    return ''        #returns an empty string if the number is not a mutliple of 7, 11, or both
       