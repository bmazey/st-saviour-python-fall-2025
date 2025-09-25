
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """
    # by using the plus sign we concatenate(add together) the strings c and s to create the new combined string
    result = c + s 
    return result

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """
    # by switching the order of the strings s and c it allows the new string to be switched in the output, kind of making the word become backwards
    result = s + c  
    return result

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """
    # the first part of the slice tells us that the character at the index of 1 will be shredded and the rest of the word will be printed 
    return s[1:] 

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """
    # using the -1 it allows the output to be the whole string except the last character 
    return s[:-1] 
