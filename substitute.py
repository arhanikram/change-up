"""
-------------------------------------------------------
Author:  Arhan Ikram
__updated__ = "2018-01-03"
-------------------------------------------------------
"""
def substitute(string, text):
    """
    -------------------------------------------------------
    Encipher a string using the letter positions.
    Use: estring = substitute(string, text):
    -------------------------------------------------------
    Preconditions:
        string - string to encipher (str)
        text - alternate text alphabet (str)
    Postconditions:
        returns
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
             "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    string = string.upper()
    words = list(string)
    
    estring = ""
    
    for i in range(len(words)):
        value = words[i]
        if value.isalpha() == False:
            estring = estring + value
        else:
            location = alpha.index(value)
            estring = estring + text[location]
    return estring
