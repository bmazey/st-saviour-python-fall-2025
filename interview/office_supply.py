
def staple_to_front(s: str, c: str) -> str:
    """
    staple_to_front() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('saviour', 'st. ') -> 'st. saviour'
    """

    # TODO

    return c + s
# pretty simple concept, front string to back string
# remember to not put return statements in '', they arent print statements.
def staple_to_end(s: str, c: str) -> str:
    """
    staple_to_end() accepts two strings s, c and returns a new string:
      - ex: staple_to_front('st. ', 'saviour') -> 'st. saviour'
    """

    # TODO

    return s + c
# also pretty simple, back string to front string
def shred_first_character(s: str) -> str:
    """
    shred_first_character() accepts a string s and returns a new string:
      - ex: shred_first_character('sst. saviour') -> 'st. saviour'
    """

    # TODO

    return s[1:]
# [x:y:z], x: start inclusive, :y: end exclusive, :z step increment

def shred_last_character(s: str) -> str:
    """
    shred_last_character() accepts a string s and returns a new string:
      - ex: shred_first_character('st. saviourr') -> 'st. saviour'
    """

    # TODO

    return s[:-1]
