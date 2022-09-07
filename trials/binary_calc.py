def binary_sum(first_bit, second_bit):
    if first_bit > second_bit:
        bigger = first_bit
    else:
        bigger = second_bit
    result = ''
    n = 1
    i = 0
    x = ''
    while i < int(bigger):
        if first_bit[len(first_bit) - n] == '1' \
                and \
                second_bit[len(second_bit) - n] == '1' \
                and \
                x != 1:
            result = '0' + result
            x = '1' + x
        elif first_bit[len(first_bit) - n] == '1' \
                and \
                second_bit[len(second_bit) - n] == '1' \
                and \
                x == 1:
            result = '1' + result
        elif first_bit[len(first_bit) - n] == '0' \
                and \
                second_bit[len(second_bit) - n] == '0' \
                and \
                x != '1':
            result = '0' + result
        elif first_bit[len(first_bit) - n] == '0' \
                and \
                second_bit[len(second_bit) - n] == '0' \
                and \
                x == '1':
            result = '1' + result
            x = ''
        elif first_bit[len(first_bit) - n] == '1' \
                and \
                second_bit[len(second_bit) - n] == '0' \
                and \
                x == '1':
            result = '0' + result
        elif first_bit[len(first_bit) - n] == '1' \
                and \
                second_bit[len(second_bit) - n] == '0' \
                and \
                x != '1':
            result = '1' + result
        elif first_bit[len(first_bit) - n] == '0' \
                and \
                second_bit[len(second_bit) - n] == '1' \
                and \
                x == '1':
            result = '0' + result
        elif first_bit[len(first_bit) - n] == '0' \
                and \
                second_bit[len(second_bit) - n] == '1' \
                and \
                x != '1':
            result = '1' + result
        n += 1
        i += 1
    return result



print(binary_sum('10', '1'))
