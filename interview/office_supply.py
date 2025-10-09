
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """

    result = c + s  # c must come before s when concatenating because order is flipped
    return result # concatenating the two strings together 

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """

    result = s + c  
    # s must come before c when concatenating two strings that are in order
    return result # concatenating but switching the order of s and c - c + s

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    return s[1: ]  # includes the entire string besides the first character

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """

    return s[ :-1]  # includes the entire string besides the last character
