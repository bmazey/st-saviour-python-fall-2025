
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # TODO implement seven_eleven function
def seven_eleven(number: int) -> str:
    if number % 7 == 0 and number % 11 == 0:
        return "seveneleven" 
    # if number goes in evening to 7 and 11 it'll run"
    if number % 7 == 0: 
    # if its just 7 it'll run one
        return "seven"
    if number % 11 == 0: 
    # if its just 11 that's all that'll show up
        return "eleven"
    return ''
