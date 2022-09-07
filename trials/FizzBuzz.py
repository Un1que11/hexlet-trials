def fizz_buzz(begin, end):
    if begin > end:
        return ''
    elif begin == end:
        return str(begin)
    else:
        result = ''
        while begin <= end:
            if int(begin) % 3 == 0 and int(begin) % 5 == 0:
                result += 'FizzBuzz' + ' '
            elif int(begin) % 3 == 0:
                result += 'Fizz' + ' '
            elif int(begin) % 5 == 0:
                result += 'Buzz' + ' '
            elif int(begin) % 3 == 0:
                result += 'Fizz' + ' '
            else:
                result += str(begin) + ' '
            begin += 1
        return result.strip()


print(fizz_buzz(11, 20))
