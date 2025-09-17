
def seven_eleven(number: int) -> str:
    """
    seven_eleven() is a function which takes a number and returns:
        - 'seven' if the number is a multiple of 7
        - 'eleven' if the number is a multiple of 11
        - 'seveneleven' if the number is a multiple of 7 and 11
        - an empty string if the number is not a multiple of 7 or 11
    """

    # TODO implement seven_eleven function
# tried % didnt work
# tried division, didnt work
# tried switching 'seven' to 7
# tries elif instead of if
# i dont get this
# as of right now i am trying random stuff ill write down something if it works

# its return not print
# idk why modulo wasnt working before but it is now and im happy
# i also dont know why number wasnt working, prolly b/c i didnt make it a command, thanks Mr Sadushi and Google for Elif and thank google for Return
def seven_eleven(number: int) -> str:
    if number % 7 == 0 and number % 11 == 0:
        return "seveneleven"
    elif number % 7 == 0:
        return "seven"
    elif number % 11 == 0:
        return "eleven"
    else:
        return ""