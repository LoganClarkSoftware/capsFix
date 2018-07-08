# lowerCase(mainIn):
#   This is used to make an input variable(any variable type that can be concatenated to a string will work) all lowercase.
#   All of the chars and return it as a string.
#
#   Var. Meaning:
#       mainIn: The main input variable. MUST be of a variable type that be concatenated to a string.
def lowerCase(mainIn):
    mainUse = list(str(mainIn))  # Concatenates input var. into string and then splits the string by char for array mainUse
    # Start Char Check
    for i in range(len(mainUse)):
        if mainUse[i] == "A":
            mainUse[i] = "a"
        if mainUse[i] == "B":
            mainUse[i] = "b"
        if mainUse[i] == "C":
            mainUse[i] = "c"
        if mainUse[i] == "D":
            mainUse[i] = "d"
        if mainUse[i] == "E":
            mainUse[i] = "e"
        if mainUse[i] == "F":
            mainUse[i] = "f"
        if mainUse[i] == "G":
            mainUse[i] = "g"
        if mainUse[i] == "H":
            mainUse[i] = "h"
        if mainUse[i] == "I":
            mainUse[i] = "i"
        if mainUse[i] == "J":
            mainUse[i] = "j"
        if mainUse[i] == "K":
            mainUse[i] = "k"
        if mainUse[i] == "L":
            mainUse[i] = "l"
        if mainUse[i] == "M":
            mainUse[i] = "m"
        if mainUse[i] == "N":
            mainUse[i] = "n"
        if mainUse[i] == "O":
            mainUse[i] = "o"
        if mainUse[i] == "P":
            mainUse[i] = "p"
        if mainUse[i] == "Q":
            mainUse[i] = "q"
        if mainUse[i] == "R":
            mainUse[i] = "r"
        if mainUse[i] == "S":
            mainUse[i] = "s"
        if mainUse[i] == "T":
            mainUse[i] = "t"
        if mainUse[i] == "U":
            mainUse[i] = "u"
        if mainUse[i] == "V":
            mainUse[i] = "v"
        if mainUse[i] == "W":
            mainUse[i] = "w"
        if mainUse[i] == "X":
            mainUse[i] = "x"
        if mainUse[i] == "Y":
            mainUse[i] = "y"
        if mainUse[i] == "Z":
            mainUse[i] = "z"
    # End Char Check
    mainOut = ""
    # Start Array To String
    for i in range(len(mainUse)):
        mainOut += mainUse[i]
    # End Array To String
    return mainOut  # Returns the string with all chars lowercase.


# upperCase(mainIn):
#   This is used to make an input variable(any variable type that can be concatenated to a string will work) all uppercase.
#   All of the chars and return it as a string.
#
#   Var. Meaning:
#       mainIn: The main input variable. MUST be of a variable type that be concatenated to a string.
def upperCase(mainIn):
    mainUse = list(str(mainIn))  # Concatenates input var. into string and then splits the string by char for array mainUse
    # Start Char Check
    for i in range(len(mainUse)):
        if mainUse[i] == "a":
            mainUse[i] = "A"
        if mainUse[i] == "b":
            mainUse[i] = "B"
        if mainUse[i] == "c":
            mainUse[i] = "C"
        if mainUse[i] == "d":
            mainUse[i] = "D"
        if mainUse[i] == "e":
            mainUse[i] = "E"
        if mainUse[i] == "f":
            mainUse[i] = "F"
        if mainUse[i] == "g":
            mainUse[i] = "G"
        if mainUse[i] == "h":
            mainUse[i] = "H"
        if mainUse[i] == "i":
            mainUse[i] = "I"
        if mainUse[i] == "j":
            mainUse[i] = "J"
        if mainUse[i] == "k":
            mainUse[i] = "K"
        if mainUse[i] == "l":
            mainUse[i] = "L"
        if mainUse[i] == "m":
            mainUse[i] = "M"
        if mainUse[i] == "n":
            mainUse[i] = "N"
        if mainUse[i] == "o":
            mainUse[i] = "O"
        if mainUse[i] == "p":
            mainUse[i] = "P"
        if mainUse[i] == "q":
            mainUse[i] = "Q"
        if mainUse[i] == "r":
            mainUse[i] = "R"
        if mainUse[i] == "s":
            mainUse[i] = "S"
        if mainUse[i] == "t":
            mainUse[i] = "T"
        if mainUse[i] == "u":
            mainUse[i] = "U"
        if mainUse[i] == "v":
            mainUse[i] = "V"
        if mainUse[i] == "w":
            mainUse[i] = "W"
        if mainUse[i] == "x":
            mainUse[i] = "X"
        if mainUse[i] == "y":
            mainUse[i] = "Y"
        if mainUse[i] == "z":
            mainUse[i] = "Z"
    # End Char Check
    mainOut = ""
    # Start Array To String
    for i in range(len(mainUse)):
        mainOut += mainUse[i]
    # End Array To String
    return mainOut  # Returns the string with all chars uppercase.


# upperCaseBySpace(mainIn):
#   This is used to make all the chars after a space (including the first char) of an input variable(any variable type that can be concatenated to a string will work) all uppercase.
#   All of the chars and return it as a string.
#
#   Var. Meaning:
#       mainIn: The main input variable. MUST be of a variable type that be concatenated to a string.
def upperCaseBySpace(mainIn):
    mainUse = list(str(mainIn))  # Concatenates input var. into string and then splits the string by char for array mainUse
    # Start Char Check
    spaceBefore = True  # Keeps track if the last char was a space
    for i in range(len(mainUse)):
        if spaceBefore:
            if mainUse[i] == "a":
                mainUse[i] = "A"
            if mainUse[i] == "b":
                mainUse[i] = "B"
            if mainUse[i] == "c":
                mainUse[i] = "C"
            if mainUse[i] == "d":
                mainUse[i] = "D"
            if mainUse[i] == "e":
                mainUse[i] = "E"
            if mainUse[i] == "f":
                mainUse[i] = "F"
            if mainUse[i] == "g":
                mainUse[i] = "G"
            if mainUse[i] == "h":
                mainUse[i] = "H"
            if mainUse[i] == "i":
                mainUse[i] = "I"
            if mainUse[i] == "j":
                mainUse[i] = "J"
            if mainUse[i] == "k":
                mainUse[i] = "K"
            if mainUse[i] == "l":
                mainUse[i] = "L"
            if mainUse[i] == "m":
                mainUse[i] = "M"
            if mainUse[i] == "n":
                mainUse[i] = "N"
            if mainUse[i] == "o":
                mainUse[i] = "O"
            if mainUse[i] == "p":
                mainUse[i] = "P"
            if mainUse[i] == "q":
                mainUse[i] = "Q"
            if mainUse[i] == "r":
                mainUse[i] = "R"
            if mainUse[i] == "s":
                mainUse[i] = "S"
            if mainUse[i] == "t":
                mainUse[i] = "T"
            if mainUse[i] == "u":
                mainUse[i] = "U"
            if mainUse[i] == "v":
                mainUse[i] = "V"
            if mainUse[i] == "w":
                mainUse[i] = "W"
            if mainUse[i] == "x":
                mainUse[i] = "X"
            if mainUse[i] == "y":
                mainUse[i] = "Y"
            if mainUse[i] == "z":
                mainUse[i] = "Z"
            spaceBefore = False
        if mainUse[i] == " ":
            spaceBefore = True
    # End Char Check
    mainOut = ""
    # Start Array To String
    for i in range(len(mainUse)):
        mainOut += mainUse[i]
    # End Array To String
    return mainOut  # Returns the string with all chars after spaces uppercase.
