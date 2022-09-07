def rotate_left(triple):
    result = (triple[1], triple[2], triple[0])
    return result


def rotate_right(triple):
    result = (triple[2], triple[0], triple[1])
    return result


triple = ('dfgdfg', 234234, True)
print(rotate_left(triple))
