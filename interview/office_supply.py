def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """
    # Staple c to the front of s using string concatenation 
    result = c + s  # New string with c attached to the front of s
    return result  # Return the new string

def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """
    # Staple c to the end of s using string concatentation
    result = s + c  # Create a new string with c attached to the end of s
    return result  # Return the new string 

def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """
    # Slice the first character from s
    return s[1:]  # Return the string without the second character

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """
    # Slice the last character from s
    return s[:-1]  # Return the string without the last character