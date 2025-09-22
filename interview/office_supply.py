
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """
    # sby using the plus sign we concatenate the strings c and s to create the new combined string
    result = c + s 
    return result

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """
    # by switching the order of the strings s and c it allows the new string to be switched in the output
    result = s + c  
    return result

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    # the first part of the slice allows the output to start from that index and it is inclusive starting from the first index
    return s[1: ] 

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """
    # using the -1 it allows the output to be the opposite of the string
    return s[ :-1] 