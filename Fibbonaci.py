def fibbonaci(spot):
    first = 0
    second = 1
    for i in range(spot+2):
        first, second = second, first + second
    return first