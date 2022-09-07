def fib(serial_number):
    f0 = 0
    f1 = 1
    if serial_number == 0:
        return f0
    elif serial_number == 1:
        return f1
    else:
        while serial_number > 1:
            f = f0 + f1
            f0, f1 = f1, f
            serial_number -= 1
        return f1
