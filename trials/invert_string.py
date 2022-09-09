def invert_case(string):
    result = ''
    for symbol in string:
        if symbol == symbol.upper():
            result += symbol.lower()
        else:
            result += symbol.upper()
    return result
